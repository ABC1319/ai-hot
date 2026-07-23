+++
title = "人工智能最重要的协议变得更容易使用"
description = "在新系统下，该协议将在服务器端对会话 ID 采取更宽松的“无状态”方法，类似于大多数普通网站的工作方式"
seo_title = "人工智能最重要的协议变得更容易使用｜AI资讯解读 - AI热榜"
seo_description = "在新系统下，该协议将在服务器端对会话 ID 采取更宽松的“无状态”方法，类似于大多数普通网站的工作方式"
seo_keywords = "人工智能最重要的协议变得更容易使用, TechCrunch AI, AI新闻, AI资讯, AI热榜"
slug = "9afbcd831bf6"
type = "news"

[params]
id = "9afbcd831bf6"
name = "人工智能最重要的协议变得更容易使用"
title_en = "Analysis: AI’s most important protocol is getting a little bit easier to use"
original_url = "https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/"
source = "TechCrunch AI"
published = "2026-07-20T20:50:40"
lang = "en"
intro = "在新系统下，该协议将在服务器端对会话 ID 采取更宽松的“无状态”方法，类似于大多数普通网站的工作方式"
ai_summary = "在新系统下，该协议将在服务器端对会话 ID 采取更宽松的“无状态”方法，类似于大多数普通网站的工作方式"
summary = "Under the new system, the protocol will take a looser, \"stateless\" approach to session IDs on the server side, similar to how most ordinary websites already work."
summary_zh = "在新系统下，该协议将在服务器端对会话 ID 采取更宽松的“无状态”方法，类似于大多数普通网站的工作方式"
tags = []
list_page = 16
+++

<!-- AUTO-GENERATED: news page -->

The Model Context Protocol (MCP) is one of the basic building blocks of AI interoperability, giving AI models a secure way to access external data sources and services.

It’s the plumbing that lets a chatbot reach into your calendar, your database, or your internal tools, instead of engineers building custom pipes for every connection.

Next week, that protocol is getting a significant update, and while it might not be noticeable to end users, it could make a big difference in how the ecosystem develops.
The official spec for the new version has been public since May, but we got an unusually clear explanation of the changes Monday morning from the folks at Arcade — a two-year-old startup that’s built its entire business around the work of getting AI agents to actually function inside real companies, letting them securely connect to and act on tools like Gmail, Slack, and Salesforce.
Arcade raised $60 million in June based on the idea that most AI agents don’t fail because the underlying models are weak but because the infrastructure around them isn’t ready yet, and that’s what this update is trying to address.

Essentially, MCP is changing the way it handles session IDs — the little tokens that servers use to remember “ah, this is the same conversation as five seconds ago” — so servers can operate more easily at a larger scale.
As Arcade founder Nate Barbettini puts it:
[Under the current system] The first time an MCP client like Claude connects to a server, it sends a “hello”: I’m Claude, here’s my version, here are my capabilities.

The server replies with its own capabilities and hands back a session ID… From then on, the client sends that session ID on every request so the server knows it’s the same conversation.

Sometimes the ID expires, so the client has to notice, request a new one, and carry on….
Picture a real deployment.

You’re running a server for millions of users, behind a load balancer whose entire job is to route each request to whatever server in the farm is free, sometimes in a different region.

Now every one of those machines has to know about a session ID that some other machine handed out.

It’s not impossible, but it’s a serious pain, and it fights the load balancer instead of working with it.
In other words, the current setup assumes one server remembers you, but real companies spread traffic across dozens of servers that don’t talk to each other by default, so today’s MCP servers have to do extra work just to keep track of who’s who.

That’s been a significant headache for anyone running an MCP server at scale, and part of the reason we haven’t seen more companies ship large-scale, first-party MCP integrations despite all the hype around agentic AI this year.
Under the new system, the protocol will take a looser, “stateless” approach to session IDs on the server side, similar to how most ordinary websites already work, which should make the whole system a lot easier to maintain and, in theory, cheaper to run at scale.
That’s all pretty technical, but it’s an important reminder that not every part of AI development is moving at breakneck speeds.

While model training races ahead, a lot of the technical infrastructure those models need is still subject to the slow log-rolling of standards-body consensus.

It really is happening; it’s just a little slower!

## 🔗 原始来源

如果你要核对细节，可以再看原文：
[TechCrunch AI原文链接](https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/)

