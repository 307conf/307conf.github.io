+++
date = 2025-12-13T17:40:00-03:00
title = 'A Case Study of Fullmetal’s PyArmor Usage'
authors = ["otavio-meneghesso"]
track = "main"
short_description = "How malware abuses public obfuscators, illustrated through the FULLMETAL case and an in-depth look at PyArmor’s internals and tooling."
summary = "Otavio Meneghesso presents a technical study on how malware families leverage public obfuscators, focusing on the FULLMETAL case and on his contributions to the Pyarmor-Tooling project."
slides = "/slides/a-case-study-of-fullmetals-pyarmor-usage.pdf"
+++

This presentation by Otavio Meneghesso examines how malware families take advantage of public obfuscators, using the FULLMETAL campaign — named and reverse-engineered by him — as a case study.

Although the FULLMETAL sample provides the initial context, the main focus of the talk is to discuss his contributions to the Pyarmor-Tooling repository maintained by GDATA and to explain, in detail, how PyArmor works internally.

Otavio covers the different protection modes of PyArmor, its features, and the internal mechanisms of the BCC (Bytecode-to-C Compiler) mode — which even produces ELF binaries in Windows environments — along with remarks on the JIT mode and Python runtime patches required for analysis. He also discusses relevant aspects of the Binary Ninja API and revisits essential elements of Python bytecode.

The presentation concludes with a practical demonstration of the script he developed to port the original analysis from IDA to Binary Ninja.
