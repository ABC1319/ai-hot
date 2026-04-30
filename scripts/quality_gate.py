#!/usr/bin/env python3
import json, sys
import re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SITE_CONTENT = ROOT / 'site' / 'content'

def zh_ratio(text):
    text = str(text or '').strip()
    letters = sum(c.isalpha() or ('\u4e00' <= c <= '\u9fff') for c in text)
    zh = sum('\u4e00' <= c <= '\u9fff' for c in text)
    return zh / max(letters, 1)

def fail(msg):
    print('❌', msg)
    return 1

def check_models_curated(errors):
    path = DATA / 'models_curated.json'
    if not path.exists():
        errors.append('models_curated.json missing')
        return
    data = json.loads(path.read_text(encoding='utf-8'))
    items = data.get('items') or []
    names = [str(x.get('name') or '') for x in items]
    urls = [str(x.get('url') or '') for x in items]
    blobs = [f"{n} {u}".lower() for n, u in zip(names, urls)]
    required = ['gpt-5.5', 'ling-2.6', 'minimax-m2.7', 'deepseek-v4']
    for key in required:
        if not any(key in b for b in blobs):
            errors.append(f'models missing required hot model: {key}')

    stale_patterns = [r'deepseek-v3\.2', r'qwen3\.5', r'mimo-32b']
    stale_hits = []
    for b, n in zip(blobs, names):
        if any(re.search(p, b) for p in stale_patterns):
            stale_hits.append(n)
    if stale_hits:
        errors.append(f'models contain superseded old versions: {stale_hits[:10]}')

    bad_icons = []
    for x in items:
        icon = str(x.get('icon_url') or x.get('icon') or '')
        if not icon:
            bad_icons.append(x.get('name'))
        elif 'openrouter.ai/favicon' in icon or 'github.com/favicon' in icon:
            bad_icons.append(x.get('name'))
    if bad_icons:
        errors.append(f'models fake/missing icons: {bad_icons[:10]}')

    category_ids = [c.get('id') for c in data.get('categories') or []]
    expected = ['top', 'coding', 'multimodal', 'image', 'video', 'open', 'watch']
    ordered = [c for c in category_ids if c in expected]
    if ordered != expected[:len(ordered)]:
        errors.append(f'model category order unexpected: {category_ids}')

def check_readme_sync(errors, expected_date):
    readme = ROOT / 'README.md'
    if not readme.exists():
        return
    text = readme.read_text(encoding='utf-8')
    if expected_date and expected_date not in text:
        errors.append(f'README date not synced with data date: missing {expected_date}')

def main():
    errors=[]
    check_models_curated(errors)

    agents=json.loads((DATA/'agents.json').read_text(encoding='utf-8'))
    missing=[a.get('name') for a in agents if not (a.get('icon') or a.get('logo') or a.get('emoji') or a.get('icon_url'))]
    if missing:
        errors.append(f'agents missing icons: {missing[:10]}')
    english_agents=[]
    for a in agents:
        desc=str(a.get('description') or '').strip()
        if len(desc) < 8 or zh_ratio(desc) < 0.35:
            english_agents.append(a.get('name') or a.get('id'))
    if english_agents:
        errors.append(f'agents descriptions not Chinese enough: {english_agents[:10]}')

    for filename in ['tools.json', 'agents.json']:
        records = json.loads((DATA / filename).read_text(encoding='utf-8'))
        bad_icons = []
        missing_icon_url = []
        for item in records:
            icon_url = str(item.get('icon_url') or '')
            icon = str(item.get('icon') or item.get('logo') or '')
            if not icon_url:
                missing_icon_url.append(item.get('name') or item.get('id'))
            if (icon_url and ('github.com/favicon' in icon_url or 'openrouter.ai/favicon' in icon_url)) or (icon and ('github.com/favicon' in icon or 'openrouter.ai/favicon' in icon)):
                bad_icons.append(item.get('name') or item.get('id'))
        if missing_icon_url:
            errors.append(f'{filename} missing icon_url: {missing_icon_url[:10]}')
        if bad_icons:
            errors.append(f'{filename} fake icons: {bad_icons[:10]}')

    list_tpl = (ROOT / 'site' / 'layouts' / '_default' / 'list.html').read_text(encoding='utf-8')
    if 'https://www.google.com/s2/favicons?domain={{ $modelDomain }}' in list_tpl or 'https://www.google.com/s2/favicons?domain={{ $toolDomain }}' in list_tpl:
        errors.append('models/tools/agents templates still derive generic favicons from item URL instead of using icon_url')
    if '.icon_url' not in list_tpl:
        errors.append('list template does not render icon_url')

    hot=json.loads((DATA/'hot.json').read_text(encoding='utf-8'))
    items=hot.get('top_20') or hot.get('items') or []
    if not items:
        errors.append('hot list is empty')
    for idx,item in enumerate(items[:10],1):
        nid=item.get('news_id')
        title=item.get('title_zh') or item.get('title') or ''
        summary=item.get('ai_summary') or item.get('subtitle') or item.get('description') or ''
        if item.get('type') != 'news':
            errors.append(f'hot #{idx} not news: {title}')
        if not nid:
            errors.append(f'hot #{idx} missing news_id: {title}')
        elif not ((SITE_CONTENT/'news'/f'{nid}.md').exists() or (SITE_CONTENT/'news'/str(nid)/'index.md').exists()):
            errors.append(f'hot #{idx} missing generated page: /news/{nid}/')
        if zh_ratio(title) < 0.35:
            errors.append(f'hot #{idx} title not Chinese enough: {title}')
        if zh_ratio(summary) < 0.45:
            errors.append(f'hot #{idx} summary not Chinese enough: {summary[:80]}')

    briefing=json.loads((DATA/'briefing.json').read_text(encoding='utf-8'))
    meta=json.loads((DATA/'meta.json').read_text(encoding='utf-8'))
    tz=ZoneInfo('Asia/Shanghai')
    last_update_raw=str(meta.get('last_update') or '').strip()
    try:
        last_update=datetime.strptime(last_update_raw, '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz)
    except ValueError:
        errors.append(f'meta last_update invalid: {last_update_raw}')
    else:
        age_hours=(datetime.now(tz)-last_update).total_seconds()/3600
        if age_hours > 8:
            errors.append(f'data stale: last_update {last_update_raw}, age {age_hours:.1f}h')
        expected_date=last_update.strftime('%Y-%m-%d')
        if briefing.get('date') != expected_date:
            errors.append(f'briefing date mismatch current data: {briefing.get("date")} != {expected_date}')
        check_readme_sync(errors, expected_date)

    if errors:
        for e in errors:
            print('❌', e)
        return 1
    print('✅ quality gate passed')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
