# Guia rápido para criar conteúdo no site da 307 Conf

O projeto é um site Hugo multilíngue (pt-br e en) com conteúdo separado por seção (`authors`, `presentations`, `villages`, `trainings`, etc.). Este guia lista como criar e relacionar cada tipo de conteúdo seguindo os padrões já usados.

## Convenções gerais
- Crie o mesmo conteúdo nos dois idiomas (`content/pt-br` e `content/en`) usando o mesmo slug (nome do arquivo em kebab-case).
- O front matter é TOML entre `+++`. Use `draft = true` enquanto escreve e troque para `false` na publicação.
- Datas/horários: use ISO 8601 com fuso `-03:00` (ex.: `2025-12-13T11:00:00-03:00`). O site já está com `buildFuture = true`.
- Imagens ficam em `static/images/...` e são referenciadas com caminho absoluto (ex.: `/images/speakers/nome.png`).
- `weight` define a ordem em listas (villages, trainings). Em palestras a ordem é pelo `date`.
- Comandos básicos:
  - Autor: `hugo new --kind authors content/pt-br/authors/slug.md`
  - Palestra: `hugo new --kind presentations content/pt-br/presentations/slug.md`
  - Village: `hugo new content/pt-br/villages/slug/_index.md` (usa o archetype padrão)
  - Training: `hugo new content/pt-br/trainings/slug.md`

## Autores (`content/<lang>/authors/`)
- Campos usados: `title` (nome), `slug`, `role` (cargo/linha do job title), `avatar` (1:1). O corpo do Markdown é a bio.
- O slug do autor é o valor que deve ser colocado em `authors = ["slug"]` dentro das palestras para o site linkar a bio automaticamente.
- Exemplo:

```toml
+++
title = "Fulana da Silva"
slug = "fulana-da-silva"
role = "Security Researcher"
avatar = "/images/speakers/fulana.png"
draft = false
+++

Bio em um ou dois parágrafos, descrevendo especialidade e pesquisas.
```

## Palestras (`content/<lang>/presentations/`)
- Campos principais:
  - `title`: título exibido.
  - `date`: data/hora (usado para ordenar agenda e agrupar por dia).
  - `authors`: lista de slugs dos autores.
  - `track` **ou** `tracks`: nome da trilha. Use o valor da village quando a talk pertencer a uma village (veja seção abaixo).
  - `short_description`: resumo curto (cards).
  - `summary`: resumo maior; o corpo do Markdown traz o texto completo.
  - `logo`: imagem do(a) palestrante (opcional).
  - `location`: sala ou espaço (opcional).
  - `period`: texto ou horário exibido; se não informar, o site mostra `date` no formato `datetime_format`.
  - `placeholder = true`: para blocos de agenda sem conteúdo (ex.: almoço/credenciamento) que não geram link.
- Exemplo de talk na trilha principal:

```toml
+++
title = "Heap primitives para além do usual"
date = 2025-12-13T14:00:00-03:00
authors = ["fulana-da-silva", "beltrano-sousa"]
track = "main"
short_description = "Demonstração prática de primitivas de heap em cenários reais."
summary = "Versão expandida do resumo curto. Use para dar contexto extra."
location = "Auditório Principal"
draft = false
+++

Conteúdo detalhado da palestra aqui.
```

## Palestras de villages
- Cada village define um `track` (veja abaixo). Para que a palestra apareça na agenda daquela village e na página geral de villages, use **o mesmo valor de `track`** no front matter da talk.
- Se precisar de mais de uma trilha, use `tracks = ["Binary Exploitation Village", "Main"]`.
- Mantenha os slugs e valores de `track` consistentes nos dois idiomas (ajustando apenas o texto se houver tradução).
- Exemplo de talk atrelada a uma village:

```toml
+++
title = "Introdução prática a exploitation em ARM"
date = 2025-12-14T10:30:00-03:00
authors = ["fulana-da-silva"]
track = "Binary Exploitation Village" # deve ser igual ao track definido na village
short_description = "Laboratório guiado de ROP e mitigação em ARM."
summary = "Detalhe mais o formato do laboratório, pré-requisitos e nível esperado."
location = "Village: Binary Exploitation"
draft = false
+++
```

## Villages (`content/<lang>/villages/<slug>/_index.md`)
- Cada village é uma pasta com `_index.md` (página de seção). Campos recomendados:
  - `title`: nome da village.
  - `track`: **obrigatório**. Identificador textual que precisa casar com o `track` das palestras dessa village.
  - `logo`: imagem redonda exibida no carrossel e cards.
  - `location`: sala/área (opcional).
  - `weight`: ordenação na lista/carrossel (menor vem primeiro).
  - Corpo do Markdown: descrição da atividade/hands-on (opcional, mas recomendado).
- Exemplo:

```toml
+++
title = "Binary Exploitation Village"
track = "Binary Exploitation Village"
location = "Espaço Villages 1"
weight = 1
draft = false
+++

Texto explicando o que o público vai encontrar, requisitos e curadoria.
```

## Trainings (`content/<lang>/trainings/`)
- Não há archetype dedicado; use o template padrão e preencha:
  - `title`
  - `date` (início do treinamento)
  - `short_description` e `summary`
  - `image` (banner 1280×720 recomendado)
  - `link` (inscrição ou landing page)
  - `sponsors` (lista) ou `sponsor` (string) para exibir selos
  - `weight` (ordenação)
- Exemplo:

```toml
+++
title = "Red Team em infra OT"
date = 2025-12-12T09:00:00-03:00
short_description = "Treinamento mão na massa sobre ataques em ambientes industriais."
summary = "Programa, pré-requisitos e laboratórios que serão cobertos."
image = "/images/trainings/red-team-ot.png"
link = "https://example.com/rt-ot"
sponsors = ["Parceiro X", "Laboratório Y"]
weight = 1
draft = false
+++
```

## Agenda e páginas estáticas
- `content/<lang>/agenda/_index.md` usa `tracks = ["main", ...]` para filtrar quais trilhas aparecem na agenda e `datetime_format` para formatar horários (padrão `HH:mm`). A timeline da home usa `params.tracks` em `hugo.toml`.
- `content/<lang>/ctf/`, `cfp/`, `tickets/`, `about/` seguem o archetype padrão; basta editar o Markdown e manter a versão em ambos os idiomas.

## Checklist antes de publicar
- Gerar os dois idiomas com o mesmo slug e valores compatíveis (`track`, `authors`, etc.).
- Garantir que as imagens estejam em `static/images/...` e referenciadas com caminho absoluto.
- Ajustar `draft = false` quando estiver pronto.
- Conferir no servidor local: `HUGO_CACHEDIR="$(pwd)/.hugo_cache" hugo server -D`
- Validar se os horários caem nos dias do evento (13 e 14/12/2025) para aparecerem na agenda.
