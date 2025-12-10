# Contributing Guidelines — 307 Conf site

Obrigado por contribuir! Para evitar publicações com front matter incorreto, siga estas convenções ao criar novas páginas (especialmente apresentações e autores).

## Formato de front matter
- Este repositório usa por convenção TOML (`+++`) no front matter. Hugo suporta TOML/YAML/JSON, entretanto para consistência prefira TOML.
- Use `hugo new` com os archetypes fornecidos para gerar front matter correto.

## Apresentações (Presentations / Talks)
- Local: `content/<lang>/presentations/<slug>.md` (ex.: `content/pt-br/presentations/minha-palestra.md`).
- Campo `authors` deve ser um array de slugs que correspondem aos arquivos em `content/<lang>/authors/`.

Exemplo (TOML):
```
+++
title = "Nome da apresentação"
date = 2025-12-13T10:00:00-03:00
authors = ["joao-vitor-keowu"]     # array de slugs do autor
period = "TDB"                     # opcional: pode ser string ou ISO datetime
location = "Sala 1"
short_description = "Breve descrição para cards e listagens"
summary = "Resumo mais longo para a página da apresentação"
logo = "/images/speakers/autor.png"
weight = 1
+++
```

- Campos úteis (opcionais):
  - `author` — sobrescreve o nome do autor exibido
- `author_link` — link para a página do autor (opcional)
  - `period` — se deseja um período específico para esta apresentação
  - `location`, `short_description`, `summary`, `logo`, `weight`

## Autores (Authors)
- Local: `content/<lang>/authors/<slug>.md`.
- O `slug` que você usa em `authors = ["..."]` geralmente é o nome do ficheiro (sem extensão). Você pode também definir `slug = "..."` na front matter do autor.

Exemplo (TOML):
```
+++
title = "João Vitor (@keowu)"
description = "Pesquisador em..."
date = 2025-11-12T09:00:00-03:00
slug = "joao-vitor-keowu"
role = "Sr. Security Researcher"
+++
```

## params.period (período global do evento)
- Em `hugo.toml` você pode definir `params.period` como fallback global do evento. Exemplo (TOML):
```
[params]
period = [
  2025-12-13T10:00:00-03:00,
  2025-12-14T18:00:00-03:00,
]
```
- Os templates usarão o `period` da página quando este existir, caso contrário usarão `site.Params.period`.

## Archetypes
Neste repositório há archetypes para criar novo conteúdo com front matter correto:
- `archetypes/presentation.md` — para `hugo new content/<lang>/presentations/<slug>.md`
- `archetypes/author.md` — para `hugo new content/<lang>/authors/<slug>.md`

Use `hugo new` para gerar arquivos já com front matter compatível.

## Checklist antes de abrir PR / criar conteúdo
- [ ] Use TOML (`+++`) no front matter.
- [ ] Confirme que `authors` é um array de slugs existentes.
- [ ] Verifique URLs e imagens (`logo`, `profile_image`) apontam para `static/` ou caminhos públicos válidos.
- [ ] Teste localmente com `hugo server -F` e verifique a renderização.

Obrigado e bom trabalho! Se quiser, abra uma issue e eu posso revisar o front matter antes do merge.
