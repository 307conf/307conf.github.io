# 307 Conf Website

Site da 307 Temporary Security Conference, construído com [Hugo](https://gohugo.io/).

## Setup

### Requisitos

- **Hugo extended ≥ 0.152**

### Instalar e executar localmente

```bash
# Instale o Hugo
brew install hugo

# Execute o servidor de desenvolvimento
HUGO_CACHEDIR="$(pwd)/.hugo_cache" hugo server -D
```

Use `-D` para visualizar conteúdo em rascunho (`draft = true`).  
Acesse em `http://localhost:1313`.

## Criando conteúdo

O projeto usa **archetypes** para padronizar a criação de conteúdo. Use o comando `hugo new` para criar novos posts com o template correto.

> ⚠️ **Importante**: Todo conteúdo deve ser criado nos **dois idiomas** (`pt-br` e `en`) para manter o site em sincronia.

### Autores (Authors)

Criar novo autor em português:
```bash
hugo new content/pt-br/authors/seu-nome.md
```

Criar novo autor em inglês:
```bash
hugo new content/en/authors/seu-nome.md
```

O archetype gera um template com os campos:
- `title` - Nome do autor
- `description` - Bio curta ou especialidade
- `slug` - Identificador único (ex: `maria-silva`)
- `role` - Cargo ou posição
- `avatar` - Caminho para imagem (ex: `/images/speakers/maria-silva.png`)

### Apresentações (Talks)

Criar nova apresentação em português:
```bash
hugo new presentations/nome-da-talk.md
```

Criar em inglês:
```bash
hugo new presentations/nome-da-talk.md
```

Campos principais:
- `title` - Título da palestra
- `date` - Data/hora (formato ISO 8601, ex: `2025-12-13T11:00:00-03:00`)
- `authors` - Lista de slugs de autores (ex: `["maria-silva", "joao-santos"]`)
- `period` - Horário exibido (ex: `"13 Dez · 11:00 · Sala 2"`)
- `location` - Local/trilha (ex: `"Sala 2"`)
- `short_description` - Resumo para cards
- `summary` - Descrição completa
- `logo` - Imagem do speaker (ex: `/images/speakers/maria-silva.png`)

### Treinamentos (Trainings)

Criar novo treinamento:
```bash
hugo new trainings/nome-do-treinamento.md
```

Campos:
- `title` - Nome do treinamento
- `date` - Data de início
- `short_description` - Resumo para cards
- `summary` - Descrição detalhada
- `image` - Banner do treinamento (ideal: 1280×720)
- `link` - URL de inscrição

### Villages

Criar nova village:
```bash
hugo new villages/nome-da-village.md
```

Campos:
- `title` - Nome da village
- `date` - Horário inicial
- `tags` - Categorias (ex: `["hardware", "sdr", "iot"]`)
- `summary` - Descrição

## Estrutura do projeto

```
content/          # Conteúdo Markdown por idioma (pt-br, en)
archetypes/       # Templates para novos posts
data/             # Dados TOML (patrocinadores, apoiadores)
static/images/    # Imagens servidas em /images/
themes/noir/      # Tema Hugo
i18n/             # Traduções de strings
public/           # Build final (gerado automaticamente)
```

## Dicas importantes

- **Slugs**: Use o mesmo `slug` nos dois idiomas para que autores e apresentações sejam relacionadas automaticamente.
- **Imagens**: Coloque em `static/images/` e referencie com caminho absoluto (ex: `/images/speakers/nome.png`).
- **Front matter**: Mantenha o formato TOML (`+++ … +++`).
- **Rascunhos**: Arquivos com `draft = true` só aparecem com `hugo server -D`.


