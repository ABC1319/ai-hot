+++
title = "德国AI联盟发布Soofi S，开放30B模型超越基准"
description = "文章网址：https://the-decoder.com/german-ai-consortium-releases-s…"
seo_title = "德国AI联盟发布Soofi S，开放30B模型超越基准｜AI资讯解读 - AI热榜"
seo_description = "文章网址：https://the-decoder.com/german-ai-consortium-releases-s…"
seo_keywords = "德国AI联盟发布Soofi S，开放30B模型超越基准, Hacker News AI, AI新闻, AI资讯, AI热榜"
slug = "ac82ff3dcf1e"
type = "news"

[params]
id = "ac82ff3dcf1e"
name = "德国AI联盟发布Soofi S，开放30B模型超越基准"
title_en = "Report: German AI consortium releases Soofi S, an open 30B model that tops benchmarks"
original_url = "https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/"
source = "Hacker News AI"
published = "2026-07-16T17:44:46"
lang = "en"
intro = "文章网址：https://the-decoder.com/german-ai-consortium-releases-s…"
ai_summary = "文章网址：https://the-decoder.com/german-ai-consortium-releases-s…"
summary = "Article URL: https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/ Comments URL: https://news."
summary_zh = "文章网址：https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-englis…"
tags = []
list_page = 34
+++

<!-- AUTO-GENERATED: news page -->

German AI consortium releases Soofi S, an open 30B model that tops benchmarks in both English and German
Key Points
- A German research consortium has released the open-source language model Soofi S, which was trained entirely on Deutsche Telekom's AI cloud infrastructure.
- The model uses a resource-efficient hybrid architecture that activates only 3.2 of its 31.6 billion parameters per token, keeping processing speed constant even with very long inputs.
- With a strong focus on German training data, Soofi S outperforms other fully open models, such as Olmo 3 32B and Apertus 70B, in benchmarks for German, English, and programming tasks.
Update –
- Statement on the allegation of overtraining added
Update from July 15, 2026:
After launch, critics argued that Soofi S was heavily "overtrained" by the standards of the classic Chinchilla scaling laws.

Google DeepMind published those laws in 2022, describing how to balance model size and training data for a fixed compute budget.

The sweet spot they identified was roughly 20 tokens per parameter.

Soofi S blows past that ratio.

With about 27 trillion tokens and 30 billion parameters, it lands at several hundred to one.

Factor in only the 3.2 billion parameters active per token, and the ratio jumps to several thousand to one.
Michael Fromm, part of the project's technical leadership, pushes back on that criticism.

He argues those rules don't simply carry over to Mixture-of-Experts (MoE) architectures.

"There's new research showing that the old scaling laws from dense models no longer apply to MoE architectures," Fromm said.

The reason comes down to how MoE models are built.

Individual experts benefit from seeing the same documents, so repeated data in a large, high-quality dataset is less of a problem than it would be with dense models.

As a point of comparison, Fromm points to Nvidia, which trained its own models on up to 25 trillion tokens.

## 🔗 原始来源

如果你要核对细节，可以再看原文：
[Hacker News AI原文链接](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/)

