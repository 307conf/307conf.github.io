+++
title = "Vulnerabilidades Persistentes no Protocolo CAN BCM do Kernel do Linux: Uma Análise de Exploração e Descoberta"
date = 2025-11-12T10:00:00-03:00
authors = ["anderson-nascimento"]
period = "A definir horário"
location = "A definir sala"
track = "main"
short_description = "Análise de falhas persistentes no protocolo CAN BCM do kernel Linux, exploração prática e desafios no processo de patching."
summary = "Anderson Nascimento apresenta sua experiência na descoberta e exploração de múltiplas vulnerabilidades no protocolo CAN BCM do kernel do Linux, discutindo falhas persistentes, padrões de insegurança e limitações nos processos de correção."
logo = "/images/speakers/anderson-nascimento.png"
weight = 1
+++

Em 2020, Anderson Nascimento iniciou sua pesquisa sobre o protocolo CAN BCM no kernel do Linux ao desenvolver um exploit para uma vulnerabilidade do tipo use-after-free read. Apesar de corrigida no upstream, a falha ainda afetava versões recentes de várias distribuições Linux, revelando lacunas significativas no processo de patching do ecossistema. Seu exploit demonstrava a gravidade do problema ao permitir que um usuário não privilegiado acessasse arquivos privilegiados e lesse endereços de memória de processos arbitrários.

Anos depois, ao revisitar o mesmo componente, Anderson identificou um padrão de vulnerabilidades. Uma nova falha — também corrigida em upstream — continuava presente nas versões mais atuais de distribuições populares. Ele então desenvolveu outro exploit capaz de realizar vazamento de informações privilegiadas e anular mitigações de segurança do kernel.

Durante a documentação dessa segunda vulnerabilidade, percebeu que a correção aplicada era inefetiva, possibilitando explorar novamente o mesmo comportamento e levando à descoberta de uma terceira falha, desta vez um 0-day no componente procfs do CAN BCM. Além disso, identificou uma segunda vulnerabilidade 0-day não relacionada ao procfs do protocolo.

Todas as vulnerabilidades foram reportadas e posteriormente corrigidas pelos mantenedores do kernel.  
A apresentação detalha a experiência prática de Anderson na descoberta, exploração e reporte dessas falhas no protocolo CAN BCM, incluindo desafios no pipeline de correções, técnicas de exploração e aprendizados da auditoria do kernel Linux.
