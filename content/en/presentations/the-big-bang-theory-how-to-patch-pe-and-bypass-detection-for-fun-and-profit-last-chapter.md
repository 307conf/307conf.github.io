+++
title = "The Big Bang Theory – How to Patch PE and Bypass Detection for Fun and Profit (Last Chapter)"
date = 2025-12-13T14:00:00-03:00
authors = ["nelson-brito"]
track = "main"
short_description = "How PE patching can reveal weaknesses in EDR detection and help assess ransomware-focused defenses."
summary = "Researcher Nelson Brito presents how PE patching is used to expose detection gaps in EDR solutions by simulating ransomware behavior in controlled environments."
weight = 1
+++

As ransomware continues to evolve in sophistication and impact, organizations increasingly rely on Endpoint Detection and Response (EDR) solutions as a frontline defense. However, EDR is not always the best approach to detect ransomware, as it is often highly susceptible to bypass techniques. Sophisticated threat actors frequently exploit weaknesses in static and behavioral detection, allowing malicious payloads to execute undetected. This presentation introduces Portable Executable (PE) patching as a strategic method to test and expose detection weaknesses in EDR platforms, with a focus on ransomware scenarios. By altering metadata, modifying headers, injecting shellcode, or evading heuristics through subtle binary changes, security researchers can simulate realistic ransomware behavior and evaluate whether the EDR reacts appropriately. Nelson will demonstrate how PE patching can be used in controlled testing environments.