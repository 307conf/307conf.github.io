+++
title = "Ryūjin - Aprendendo o funcionamento interno de ferramentas Bin2Bin para Obfuscação de Binários Windows PE x64"
date = 2025-11-12T10:00:00-03:00
authors = ["joao-vitor-keowu"]
period = "A definir horário"
location = "A definir sala"
short_description = ""
summary = "O pesquisador João Vitor (@keowu) compartilha sua metodologia para analisar ferramentas Bin2Bin voltadas à ofuscação avançada de binários Windows."
logo = "/images/speakers/joao-vitor.png"
weight = 1
+++

Esta talk explicará o funcionamento interno de proteções comerciais Bin2Bin: estrutura e como um PE pode ser alterado pós-compilação para substituir instruções originais por outras ofuscadas. Mostrarei como extrair sequências de opcodes geradas por qualquer compilador (na demo: o MSVC), disassemblá-las, separá-las em procedimentos, criar basic blocks estruturados e aplicar passes escritos do zero para adicionar junk/code, mutação, proteção de IAT, crypter, técnicas conhecidas de anti-debug, ofuscação MBA não linear e até uma VM que gera bytecodes para instruções matemáticas básicas. Também abordaremos memória, relocações e, como bônus, apresentaremos a ideia e os passos para desofuscar instruções processadas pelo Bin2Bin usando a nova wrapper pythonic da Hex-Rays, ida-domain. Objetivo: despertar interesse e fascínio por ofuscação e desofuscação.
