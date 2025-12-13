+++
title = "Invisible Threat: Embedding a C2 Core into RTUs via SCADA Overflow SEH"
date = 2025-12-13T16:50:00-03:00
authors = ["fernando-mengali"]
track = "main"
short_description = "Como um overflow com sobrescrita de SEH em servidor SCADA pode evoluir para backdoor, C2 e manipulação direta de RTUs."
summary = "Fernando Mengali demonstra a cadeia completa de ataque contra sistemas SCADA: da exploração de um overflow com SEH à implantação de C2 persistente e manipulação de RTUs, mostrando o impacto operacional e financeiro em infraestruturas críticas."
weight = 1
+++

A palestra apresenta a jornada completa de um ataque contra infraestrutura crítica, partindo da exploração de uma vulnerabilidade de memória em um servidor SCADA por meio de um overflow com sobrescrita de SEH. A partir dessa falha, o atacante obtém controle de execução, implanta um backdoor persistente e estabelece um canal C2 para movimentação lateral no ambiente OT.

Fernando Mengali demonstra como, após o comprometimento inicial, a exploração evolui para a manipulação direta de RTUs, permitindo desde leitura de variáveis industriais até a escrita de comandos maliciosos — alterando tensões, fechando válvulas, desligando equipamentos ou causando paralisações operacionais. A simulação inclui o uso de Python para ilustrar, de forma didática, como um atacante pode interagir com dispositivos industriais, além de uma interface gráfica simples para visualizar ataques em tempo real.

A sessão também discute as consequências práticas: interrupção de processos industriais, danos físicos a equipamentos, perdas financeiras massivas e impactos sistêmicos em setores como energia, água, saneamento, óleo e gás. O objetivo é mostrar como falhas aparentemente simples — como um buffer overflow — podem escalar para cenários de caos operacional se exploradas em ambientes SCADA.
