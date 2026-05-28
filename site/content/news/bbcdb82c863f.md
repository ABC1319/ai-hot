+++
title = "ClickHouse实战：Agentic Coding，是“神”还是“坑”？"
description = "ClickHouse实战：Agentic Coding，是“神”还是“坑”？。来源：InfoQ AI。"
seo_title = "ClickHouse实战：Agentic Coding，是“神”还是“坑”？｜AI资讯解读 - AI热榜"
seo_description = "ClickHouse实战：Agentic Coding，是“神”还是“坑”？。来源：InfoQ AI。"
seo_keywords = "ClickHouse实战：Agentic Coding，是“神”还是“坑”？, InfoQ AI, AI新闻, AI资讯, AI热榜"
slug = "bbcdb82c863f"
type = "news"

[params]
id = "bbcdb82c863f"
name = "ClickHouse实战：Agentic Coding，是“神”还是“坑”？"
title_en = "ClickHouse实战：Agentic Coding，是“神”还是“坑”？"
original_url = "https://www.infoq.cn/article/OLEDsNifw48YdleTAZDg?utm_source=rss&utm_medium=article"
source = "InfoQ AI"
published = "2026-05-25T15:46:38"
lang = "zh"
intro = "ClickHouse实战：Agentic Coding，是“神”还是“坑”？。来源：InfoQ AI。"
ai_summary = ""
summary = ""
summary_zh = ""
tags = []
list_page = 12
+++

<!-- AUTO-GENERATED: news page -->

首批编码模型和代理问世至今仅一年光景，而今天，关于在实践中使用代理编码 (agentic coding) 的看法却两极分化。

一些人认为代理将取代我们所有的工作，另一些人则认为编码代理完全无用。

有人出于各种原因厌恶 AI，也有人早已陷入 AI 狂热。

如果你关注新闻，情况也无济于事：每天都是层出不穷的新一代前沿模型、更先进的工具、新的研究突破以及基准测试中令人瞩目的成绩，同时又伴随着低质量代码、安全漏洞、负面经济影响的研究报告，以及自主代理在实际工作中表现平平的结果。

在许多公司，领导层试图强制推行 AI 的使用，而员工却感到困惑和不安。

我希望避免这种困惑，并阐明我的观点。

我们在 ClickHouse 中使用编码代理，它们在特定场景下是极佳的工具。

注：我不会使用 AI 来撰写文本，因为我个人不喜欢这种方式。

我写作速度很慢，但这是我自己的方式。

一些前提假设
在我们开始之前，请允许我提出一些假设。

这些假设可能不完全正确，且难以逐一论证，但为了保持后续讨论的理性，我们姑且采纳这些假设。

大型语言模型不具备感知能力。

它们没有意识、感质 (qualia) 或灵魂。

通用人工智能 (AGI) 和超级智能短期内都不会实现。

安全的 AI 既不存在，也不可能实现。

AI 不会取代所有工作，但会取代其中一部分。

也许它会取代你的工作，不过如果你正在阅读这篇文章，根据 贝叶斯推断，这种可能性较小。

为何是现在？

Claude Code 于 2025 年 2 月问世。

我在一年前测试时，其用途有限。

它能够成功生成小型 JavaScript 应用程序，特别是那些重复编写过多次的应用，并且可以编写一次性的 Python 和 Shell 脚本。

在处理小型仓库中的各种样板任务时，它也助我一臂之力，例如 ClickBench。

然而，当我将其应用到我们的主要 C++ 代码库时，它便力不从心，生成的代码也差强人意。

无论如何，这类重复性任务很多，即使在一年前，这些 Agent 也非常有用——公司内部对它们有着实际需求。

因此，我们与 Anthropic、Windsurf 和 Cursor 签订了合作协议（解决所有法律和安全问题耗费了一些时间，并且许多问题需要在公司内部达成共识）。

我们开始使用这些 Agent，不仅限于重复性任务，还用于快速开发内部工具，例如性能测试和发布状态仪表板。

我们还推出了自研的 Agent：DWAINE、CAISER 和 TRAISA（这些名字很奇怪，因为它们是 AI 生成的），以及 SQL 控制台中的 Agent 和 AI SRE Agent。

这种趋势势不可挡，以至于我们收购了 Librechat 和 Langfuse，以增强 AI 可观测性。

## 🔗 原始来源

如果你要核对细节，可以再看原文：
[InfoQ AI原文链接](https://www.infoq.cn/article/OLEDsNifw48YdleTAZDg?utm_source=rss&utm_medium=article)

