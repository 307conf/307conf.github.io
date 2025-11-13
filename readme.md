# 307 Conf Website - Content Authoring Guide

Este repositório contém o site oficial da 307 Temporary Security Conference, construído em [Hugo](https://gohugo.io/) com o tema `noir`. Este guia explica como preparar o ambiente local e, principalmente, como criar e traduzir cada tipo de conteúdo que o site exibe.

## Stack e requisitos

- **Hugo extended ≥ 0.152** (a versão usada atualmente é 0.152.2).
- Go 1.24 é listado em `go.mod`, mas você só precisa dele caso vá atualizar o tema como módulo.
- O tema `github.com/307conf/noir` está em `themes/noir`.
- O site é multilíngue; `pt-br` é o idioma padrão e `en` a segunda língua.

### Executando localmente

```bash
# instale o hugo extended caso ainda não tenha
brew install hugo

# numa sandbox macOS, direcione o cache para dentro do repo
HUGO_CACHEDIR="$(pwd)/.hugo_cache" hugo server -D
```

- Use `-D` para incluir conteúdo com `draft = true`.
- A pasta `public/` é o destino gerado. Não edite arquivos ali; qualquer mudança será sobrescrita por `hugo`.
- Para compilar para produção: `HUGO_CACHEDIR="$(pwd)/.hugo_cache" hugo --gc`.

## Mapa do repositório

```
content/          # Markdown por idioma (pt-br, en)
data/             # Arquivos TOML que alimentam seções auxiliares (patrocinadores, apoiadores etc.)
static/           # Arquivos estáticos servidos em / (imagens, favicons, downloads)
themes/noir/      # Tema Hugo com layouts e parciais
i18n/             # Traduções de strings (ex. agendaTitle)
resources/        # Saída intermediária gerada pelo Hugo (não editar)
public/           # Build final (não editar)
```

## Fluxo geral para criar conteúdo

1. **Escolha o idioma** (`content/pt-br` ou `content/en`). Toda nova entrada precisa de versões em ambos os idiomas para manter a navegação consistente.
2. **Crie o arquivo Markdown** no diretório correto (ex.: `content/pt-br/presentations/nome-da-talk.md`).
3. **Atualize campos de front matter** em TOML (`+++ … +++`). Evite YAML para manter o padrão.
4. **Adicionar ativos**: coloque imagens em `static/images/...` e referencie-as com caminhos absolutos (`/images/...`).
5. **Verifique localmente** com `hugo server -D`.

> Dica: mantenha o mesmo `slug` para as duas línguas. Isso permite que o site relacione automaticamente palestras e bios de autores (`authors = ["slug"]`).

## Tipos de conteúdo e exemplos

### 1. Apresentações (Talks)

- Local: `content/<lang>/presentations/*.md`
- Ordenação: pelo campo `date` (UTC-3 no projeto), combinado com `weight` quando precisar forçar prioridade.
- Campos importantes:

| Campo               | Descrição                                                                 |
|---------------------|----------------------------------------------------------------------------|
| `title`             | Nome da talk mostrado no site.                                            |
| `date`              | Data/hora ISO 8601; define ordenação e permite o build com `buildFuture`.  |
| `authors`           | Lista de *slugs* que apontam para `content/<lang>/authors/<slug>.md`.      |
| `period`            | Texto curto para o horário exibido nas listagens (ex.: `"13 Dec 2025 10h"`).|
| `location`          | Sala ou trilha.                                                            |
| `short_description` | Vai para cards (home/agenda).                                              |
| `summary`           | Usado no corpo das listagens; pode conter Markdown leve.                   |
| `logo`              | Caminho para imagem do palestrante/track (ex.: `/images/speakers/foo.png`).|
| `weight`            | Inteiro opcional para forçar a ordem em seções adicionais.                 |

**Exemplo (pt-br):**

```toml
+++
title = "Forense em Pipelines Binários"
date = 2025-12-13T11:00:00-03:00
authors = ["maria-silva"]
period = "13 Dez · 11:00 · Sala 2"
location = "Sala 2"
short_description = "Como dissecar ofuscação em binários PE x64 usando apenas ferramentas open source."
summary = """
Neste talk mostramos playbooks e automações para descobrir cadeias Bin2Bin
sem depender de engines proprietárias.
"""
logo = "/images/speakers/maria-silva.png"
weight = 10
+++

Conteúdo completo da palestra (opcional) para a página individual.
```

**Exemplo (en):**

```toml
+++
title = "Reversing Binary Pipelines"
date = 2025-12-13T11:00:00-03:00
authors = ["maria-silva"]
period = "Dec 13 · 11:00 · Track 2"
location = "Track 2"
short_description = "Detect obfuscation layers inside PE x64 binaries with OSS tooling only."
summary = "Playbooks and automation pipelines for mapping Bin2Bin chains without commercial engines."
logo = "/images/speakers/maria-silva.png"
+++

Full abstract in English goes here.
```

### 2. Autores / Speakers

- Local: `content/<lang>/authors/*.md`
- O `slug` precisa ser idêntico ao valor referenciado em `authors = ["slug"]` nas apresentações.
- Campos principais: `title`, `description`, `date` (opcional, para ordenar), `slug`, `role`, além do corpo em Markdown (bio). Você pode adicionar campos opcionais como `email`, `github`, `mastodon`, `links`.

```toml
+++
title = "Maria Silva (@m4ria)"
description = "Forense e Bin2Bin pipelines"
date = 2025-12-10T09:00:00-03:00
slug = "maria-silva"
role = "Sr. Security Researcher"
github = "https://github.com/m4ria"
mastodon = "https://infosec.exchange/@m4ria"
+++

Bio em Markdown. Adicione parágrafos curtos descrevendo área de atuação,
pesquisas, talks anteriores e links úteis.
```

### 3. Trainings

- Local: `content/<lang>/trainings/*.md`
- Estas páginas alimentam tanto `/trainings/` quanto o carrossel de treinamentos na home.
- Campos úteis:

| Campo               | Uso                                                                 |
|---------------------|----------------------------------------------------------------------|
| `title`, `date`     | Nome e ordenação cronológica.                                        |
| `weight`            | Quebra empates; mais baixo vem primeiro.                             |
| `short_description` | Texto mostrado nos cards da home.                                    |
| `summary`           | Descrição no grid de `/trainings`.                                   |
| `image`             | Banner (ideal 1280×720, armazenar em `static/images/trainings/`).    |
| `link`              | URL de inscrição ou página detalhada.                                |
| `sponsors`/`sponsor`| Lista de apoiadores ou empresa que promove o curso.                  |

```toml
+++
title = "Hands-on OffSec Lab"
date = 2025-12-11T09:00:00-03:00
weight = 1
short_description = "Laboratório intensivo de 8h cobrindo evasão, Bin2Bin e engenharia reversa."
summary = "Turma enxuta (20 vagas) com foco em exercícios práticos e análise de binários ofuscados."
image = "/images/trainings/offsec-lab.jpg"
link = "https://example.com/inscricao-offsec-lab"
sponsors = ["Recon Lab", "Projeto 307"]
+++

Detalhes completos, pré-requisitos e lista de módulos.
```

### 4. Villages

- Local: `content/<lang>/villages/*.md`
- São listadas em `/villages/` e aparecerão em breve na home.

```toml
+++
title = "Hardware Hacking Village"
date = 2025-12-13T10:00:00-03:00
tags = ["hardware", "sdr", "iot"]
summary = "Banqueadas por voluntários do Garoa HC, com labs de solda rápida, SDR e fuzzing de firmware."
+++

Descrição maior, regras de participação, horário de funcionamento e links para materiais.
```

### 5. Páginas seccionais (`_index.md`)

- As páginas `agenda`, `presentations`, `trainings`, `villages`, `tickets`, `cfp` e `about` usam apenas um `_index.md` por idioma.
- Edite o texto introdutório dentro desses arquivos para atualizar avisos ou contextualizar o status da curadoria.
- Exemplo (`content/pt-br/cfp/_index.md`):

```toml
+++
title = "CFP"
+++

O Call for Presentations abre dia 30/03. Prepare sua submissão técnica ou hands-on,
com duração entre 25 e 45 minutos. Publicaremos regulamento completo nesta mesma página.
```

### 6. Dados auxiliares (`data/<lang>/*.toml`)

Algumas seções leem arquivos TOML ao invés de Markdown:

- **`data/<lang>/sponsor.toml`** - define duas linhas (`row1`, `row2`) com `{ icon, name }` para o carrossel de tecnologias/patrocinadores da home. Os ícones seguem a sintaxe do [Devicon](https://devicon.dev/).
  
  ```toml
  row1 = [
    { icon = "devicon-hugo-plain", name = "Hugo" },
    { icon = "devicon-tailwindcss-plain", name = "Tailwind" }
  ]
  row2 = [
    { icon = "devicon-go-plain", name = "Go" }
  ]
  ```

- **`data/<lang>/about.toml`** - alimenta o card de apoiadores na página "Sobre".

  ```toml
  [[supporters]]
  name = "Garoa Hacker Clube"
  date = "São Paulo, Brasil"
  url = "https://garoa.net.br/"
  ```

- **`data/<lang>/agenda.toml`** - opcional; mantém um histórico de agenda em formato TOML. Útil se quiser montar seções extras ou usar dados via shortcodes.

- **`data/<lang>/villages.toml` / `trainings.toml`** - hoje guardam placeholders, mas você pode reaproveitá-los se quiser exibir listas adicionais através de parciais personalizadas.

### 7. Assets e logos

- Coloque imagens em `static/images/...`. Durante o build elas serão servidas em `/images/...`.
- Para novos speakers crie arquivos em `static/images/speakers/<slug>.png` e referencie via front matter.
- Mantenha os arquivos otimizados (≤ 200 KB) para preservar a performance.

### 8. Traduções e menus

- Strings como `agendaTitle`, `learnMore` e `noEntriesYet` vivem em `i18n/pt-br.toml` e no arquivo equivalente para inglês (por ora herdado do tema). Para adicionar novas labels, crie entradas nos dois idiomas.
- Os itens de menu estão no `hugo.toml` dentro de `[languages.<code>.menu.main]`. Sempre adicione links equivalentes para `pt-br` e `en`.
- O herói da home usa `data/<lang>/author.toml` se existir; caso contrário, herda `[params]` de `hugo.toml` (`name`, `description`, `period`, `location`, `email`, etc.).

## Checklist antes de commitar

1. Conteúdo criado/atualizado em **ambos os idiomas**.
2. Slugs de autores e palestras correspondem (`authors = ["slug"]`).
3. Imagens salvas em `static/images/...` e referenciadas com caminho absoluto.
4. `hugo server -D` sem erros e `hugo --gc` apenas com avisos esperados.
5. `public/` não recebeu edições manuais.

Seguindo essas instruções você garante que as listagens da home, agenda, speakers, trainings e villages reflitam automaticamente o que estiver em `content/` e `data/`, mantendo o site sempre em sincronia entre português e inglês.
