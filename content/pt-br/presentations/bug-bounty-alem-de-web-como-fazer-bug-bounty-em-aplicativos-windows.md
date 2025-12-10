+++
title = "Bug bounty além de web: como fazer bug bounty em aplicativos Windows"
date = 2025-12-13T14:50:00-03:00
authors = ["giuliano-sanfins"]
short_description = "Como identificar vulnerabilidades em aplicativos Windows e explorar um ambiente pouco utilizado por bug bounty hunters."
summary = "Giuliano Sanfins apresenta vulnerabilidades reais encontradas em aplicativos Windows em programas de bug bounty e demonstra como analisar protocolos, AppServices, COM, Named Pipes e outros fundamentos que sustentam o ecossistema Windows."
logo = "/images/speakers/giuliano-sanfins.png"
track = "main"
weight = 1
+++

Quando se fala em bug bounty, o foco costuma ser aplicações Web e, no máximo, Android ou iOS. Mas há um ambiente que quase não recebe atenção: aplicativos Windows. Nesta palestra, Giuliano Sanfins apresenta os fundamentos que sustentam aplicações Windows — protocolos, AppServices, COM, Named Pipes, Symbolic Links e demais mecanismos internos — mostrando como esses componentes se tornam potenciais vetores de ataque.

A sessão aborda vulnerabilidades reais encontradas em programas de bug bounty e demonstra como analistas podem iniciar suas próprias análises, reconhecendo falhas, entendendo origens e validando impacto. O objetivo é abrir um novo território para hunters, cobrindo desde vetores que levam a elevação de privilégios (LPEs) até cenários de execução remota de código (RCEs), passando por técnicas práticas, demos e ferramentas de apoio.

A agenda inclui:
- Introdução ao universo Windows (UWA/UWP, Win32) + demo  
- Entrypoints e Integrity Levels  
- Capabilities e como analisá-las + demo  
- Comunicação entre processos (AppServices, Protocols, COM, sockets etc) + demo  
- FullTrust apps e riscos associados  
- Vulnerabilidades comuns + demo  
- Ferramentas úteis (Visual Studio, Burp Suite, Semgrep, x64dbg etc)  
