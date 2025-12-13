+++
title = "Invisible Threat: Embedding a C2 Core into RTUs via SCADA Overflow SEH"
date = 2025-12-13T16:50:00-03:00
authors = ["fernando-mengali"]
track = "main"
short_description = "How an overflow with SEH overwrite in a SCADA server can evolve into a backdoor, C2, and direct manipulation of RTUs."
summary = "Fernando Mengali demonstrates the full attack chain against SCADA systems: from exploiting an overflow with SEH overwrite to deploying persistent C2 and manipulating RTUs, showing operational and financial impact in critical infrastructures."
weight = 1
+++

The talk presents the complete journey of an attack against critical infrastructure, starting from the exploitation of a memory vulnerability in a SCADA server via an overflow with SEH overwrite. From this flaw, the attacker gains code execution, implants a persistent backdoor, and establishes a C2 channel for lateral movement in the OT environment.

Fernando Mengali demonstrates how, after the initial compromise, exploitation evolves into the direct manipulation of RTUs, enabling everything from reading industrial variables to writing malicious commands — changing voltages, closing valves, shutting down equipment, or causing operational outages. The simulation includes using Python to illustrate, in an accessible way, how an attacker can interact with industrial devices, along with a simple graphical interface to visualize attacks in real time.

The session also discusses the practical consequences: interruption of industrial processes, physical damage to equipment, massive financial losses, and systemic impacts on sectors such as energy, water, sanitation, oil, and gas. The goal is to show how apparently simple flaws — like a buffer overflow — can escalate into scenarios of operational chaos if exploited in SCADA environments.
