+++
date = 2025-12-13T17:40:00-03:00
title = 'A Case Study of Fullmetals Pyarmor Usage'
authors = ["otavio-meneghesso"]
track = "main"
short_description = "Como malwares exploram ofuscadores públicos: um estudo do caso FULLMETAL e dos mecanismos internos do PyArmor, incluindo BCC, JIT e técnicas usadas na análise e desofuscação."
summary = "Otavio Meneghesso apresenta um estudo técnico sobre como malwares exploram ofuscadores públicos, com foco no caso FULLMETAL e em suas contribuições para a ferramenta Pyarmor-Tooling."
slides = "/slides/a-case-study-of-fullmetals-pyarmor-usage.pdf"
+++

A apresentação conduzida por Otavio Meneghesso explora como famílias de malware se aproveitam de ofuscadores públicos, tomando como estudo de caso o FULLMETAL — nomeado e analisado por ele durante seu processo de engenharia reversa.

Apesar de o caso FULLMETAL ser usado como ponto de partida, o foco principal da talk é discutir suas contribuições para o repositório Pyarmor-Tooling, mantido pela GDATA, e explicar em detalhes como o PyArmor funciona internamente.

Otavio aborda os diferentes modos de proteção do PyArmor, suas funcionalidades e os mecanismos internos do modo BCC (Bytecode-to-C Compiler) — que, inclusive, gera ELF mesmo em ambiente Windows — além de comentários sobre o modo JIT e particularidades do runtime Python que precisam ser ajustadas para análise. Ele também discute pontos relevantes da API do Binary Ninja e revisita elementos essenciais do bytecode Python.

A talk termina com uma demonstração prática do script que desenvolveu para portar a análise originalmente feita no IDA para o Binary Ninja.