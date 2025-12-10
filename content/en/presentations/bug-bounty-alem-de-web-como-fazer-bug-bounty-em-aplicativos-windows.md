+++
title = "Bug Bounty Beyond the Web: How to Hunt Vulnerabilities in Windows Applications"
date = 2025-12-13T14:50:00-03:00
authors = ["giuliano-sanfins"]
track = "main"
short_description = "How to identify vulnerabilities in Windows applications and explore an environment rarely used by bug bounty hunters."
summary = "Giuliano Sanfins shares real vulnerabilities found in Windows applications via bug bounty programs and shows how to analyze protocols, AppServices, COM, Named Pipes, and other fundamentals that underpin the Windows ecosystem."
logo = "/images/speakers/giuliano-sanfins.png"
weight = 1
+++

When bug bounty comes up, the focus is usually on web applications and, at most, Android or iOS. But there is an environment that hardly gets attention: Windows applications. In this talk, Giuliano Sanfins covers the fundamentals that underpin Windows applications — protocols, AppServices, COM, Named Pipes, Symbolic Links, and other internal mechanisms — showing how these components become potential attack vectors.

The session discusses real vulnerabilities found in bug bounty programs and demonstrates how analysts can start their own investigations, spotting flaws, understanding their origins, and validating their impact. The goal is to open a new territory for hunters, covering everything from vectors that lead to privilege escalation (LPEs) to remote code execution (RCEs), with practical techniques, demos, and supporting tools.

The agenda includes:
- Introduction to the Windows universe (UWA/UWP, Win32) + demo
- Entry points and Integrity Levels
- Capabilities and how to analyze them + demo
- Inter-process communication (AppServices, Protocols, COM, sockets, etc.) + demo
- FullTrust apps and associated risks
- Common vulnerabilities + demo
- Useful tools (Visual Studio, Burp Suite, Semgrep, x64dbg, etc.)
