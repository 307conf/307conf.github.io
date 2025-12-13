#!/usr/bin/env python3
"""Generate PT-BR markdown for Apple Red Team Village & Red Team Community.

Authors: skips writing when the author file already exists (prevents overwrite).
Talks: overwrite only with --force.
"""

from __future__ import annotations

import argparse
import re
import textwrap
import unicodedata
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parent.parent
PT_PRESENTATIONS = ROOT / "content" / "pt-br" / "presentations"
PT_AUTHORS = ROOT / "content" / "pt-br" / "authors"


TALKS: Sequence[dict[str, object]] = [
    {
        "title": "Abertura Apple Red Team Village & Red Team Community",
        "date": "2025-12-13T10:00:00-03:00",
        "authors": ["logan", "zoziel"],
        "track": "Apple Red Team Village",
        "short_description": "Abertura oficial da Apple Red Team Village e Red Team Community.",
        "summary": "Abertura oficial das atividades da Apple Red Team Village e Red Team Community, apresentando a proposta da trilha e os temas que serão abordados ao longo do evento.",
        "weight": 1,
        "body": "",
    },
    {
        "title": "O ataque simples que pode derrubar uma empresa inteira",
        "date": "2025-12-13T10:20:00-03:00",
        "authors": ["lenon-stelman"],
        "track": "Red Team Community",
        "short_description": "Como ataques simples podem causar impactos críticos em organizações.",
        "summary": "Lenon Stelman apresenta um cenário realista onde um ataque aparentemente simples é suficiente para comprometer severamente uma empresa, explorando falhas humanas, técnicas e organizacionais.",
        "weight": 2,
        "body": "",
    },
    {
        "title": "The Anatomy of iOS Security in 2025",
        "date": "2025-12-13T11:10:00-03:00",
        "authors": ["bruno-sena"],
        "track": "Apple Red Team Village",
        "short_description": "Arquitetura moderna de segurança do iOS e seus mecanismos de defesa.",
        "summary": "Bruno Sena analisa a arquitetura de segurança do iOS em 2025, abordando mecanismos como Secure Boot, Secure Enclave, PAC, MIE e sandboxing.",
        "weight": 3,
        "body": "",
    },
    {
        "title": "macOS Zero Mercy: Inside the Mind of a Malware Developer",
        "date": "2025-12-13T14:30:00-03:00",
        "authors": ["zoziel"],
        "track": "Apple Red Team Village",
        "short_description": "Desenvolvimento de malware para macOS sob a ótica ofensiva.",
        "summary": "Workshop prático sobre desenvolvimento de malware no macOS, explorando bypass, persistência e execução furtiva para operações de Red Team.",
        "weight": 4,
        "body": "",
    },
    {
        "title": "Security Compliance em macOS",
        "date": "2025-12-14T10:20:00-03:00",
        "authors": ["natalia-sampaio"],
        "track": "Apple Red Team Village",
        "short_description": "Segurança e compliance em ambientes macOS.",
        "summary": "Natalia Sampaio discute segurança e compliance em macOS, abordando mecanismos de defesa, hardening, benchmarks e gestão de ambientes híbridos.",
        "weight": 5,
        "body": "",
    },
    {
        "title": "Understanding Client Fingerprinting: Bot Detection Evasion Using Fingerprint Multilayer Spoofing",
        "date": "2025-12-14T14:00:00-03:00",
        "authors": ["pedro-vitor"],
        "track": "Red Team Community",
        "short_description": "Evasão de detecção de bots via fingerprint spoofing.",
        "summary": "Pedro Vitor apresenta técnicas de evasão de detecção de bots por meio de spoofing de fingerprint em múltiplas camadas.",
        "weight": 6,
        "body": "",
    },
    {
        "title": "From Harmless PR to AWS Organization Takeover",
        "date": "2025-12-14T14:50:00-03:00",
        "authors": ["eurico-nicacio"],
        "track": "Red Team Community",
        "short_description": "Escalada de privilégios em ambientes AWS.",
        "summary": "Eurico Nicacio demonstra como um pull request aparentemente inofensivo pode levar ao comprometimento total de uma organização AWS.",
        "weight": 7,
        "body": "",
    },
    {
        "title": "Desmantelando uma Quadrilha de Fraudadores no Brasil com Táticas de Red Team",
        "date": "2025-12-14T15:40:00-03:00",
        "authors": ["gustavo-robertux"],
        "track": "Red Team Community",
        "short_description": "Red Team aplicado ao combate a fraudes reais.",
        "summary": "Gustavo Robertux apresenta como táticas de Red Team foram usadas para desmantelar uma quadrilha de fraudadores no Brasil.",
        "weight": 8,
        "body": "",
    },
    {
        "title": "Debate: Áreas de Pesquisa em Apple Devices",
        "date": "2025-12-14T17:00:00-03:00",
        "authors": ["logan", "zoziel"],
        "track": "Apple Red Team Village",
        "short_description": "Debate sobre pesquisa em segurança de dispositivos Apple.",
        "summary": "Debate aberto sobre áreas de pesquisa, desafios e oportunidades em segurança de dispositivos Apple.",
        "weight": 9,
        "body": "",
    },
]

AUTHORS: Sequence[dict[str, str]] = [
    {
        "title": "Lenon Stelman",
        "slug": "lenon-stelman",
        "role": "Cybersecurity Specialist",
        "avatar": "/images/speakers/lenon-stelman.png",
        "bio": "Especialista em cibersegurança, com atuação focada em Red Team, engenharia social e análise de ataques reais contra grandes organizações.",
    },
    {
        "title": "Bruno Sena",
        "slug": "bruno-sena",
        "role": "Offensive Security Researcher",
        "avatar": "/images/speakers/bruno-sena.jpg",
        "bio": "Cybersecurity professional focused on offensive security and mobile hacking. Founder of the MobSec Crew community and organizer of the Mobile Security Villages at BSides São Paulo and H2HC. Currently working at Thallium Security.",
    },
    {
        "title": "Zoziel",
        "slug": "zoziel",
        "role": "Malware Researcher",
        "avatar": "/images/speakers/zoziel.png",
        "bio": "Pesquisador em segurança ofensiva com foco em malware, evasão e simulações de ameaças em ambientes Apple.",
    },
    {
        "title": "Natalia Sampaio",
        "slug": "natalia-sampaio",
        "role": "Security Specialist",
        "avatar": "/images/speakers/natalia-sampaio.png",
        "bio": "Especialista em segurança de sistemas macOS, com foco em compliance, hardening e gestão de ambientes corporativos.",
    },
    {
        "title": "Pedro Vitor",
        "slug": "pedro-vitor",
        "role": "Security Researcher",
        "avatar": "/images/speakers/pedro-vitor.png",
        "bio": "Pesquisador em segurança com foco em fingerprinting, bot detection e evasão de mecanismos de defesa.",
    },
    {
        "title": "Eurico Nicacio",
        "slug": "eurico-nicacio",
        "role": "Cloud Security Researcher",
        "avatar": "/images/speakers/eurico-nicacio.png",
        "bio": "Pesquisador em segurança com foco em ambientes cloud, exploração de falhas de CI/CD e AWS.",
    },
    {
        "title": "Gustavo Robertux",
        "slug": "gustavo-robertux",
        "role": "Red Team Specialist",
        "avatar": "/images/speakers/gustavo-robertux.png",
        "bio": "Especialista em Red Team e investigação de fraudes digitais, com atuação em casos reais no Brasil.",
    },
    {
        "title": "Logan",
        "slug": "logan",
        "role": "Apple Security Researcher",
        "avatar": "/images/speakers/logan.png",
        "bio": "",
    },
]


def slugify(value: str) -> str:
    """Convert a title into a Hugo-friendly slug."""
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def render_front_matter(fields: Iterable[tuple[str, object]], *, bare_keys: set[str] | None = None) -> str:
    bare_keys = bare_keys or set()
    lines = ["+++"] + [
        f"{key} = {format_toml_value(value, bare=key in bare_keys)}" for key, value in fields
    ]
    lines.append("+++")
    return "\n".join(lines)


def format_toml_value(value: object, *, bare: bool = False) -> str:
    if isinstance(value, list):
        items = ", ".join(f'"{item}"' for item in value)
        return f"[{items}]"
    if bare:
        return str(value)
    if isinstance(value, str):
        return f'"{value}"'
    return str(value)


def build_presentation_entry(talk: dict[str, object]) -> tuple[Path, str]:
    slug = slugify(str(talk["title"]))
    front_matter = render_front_matter(
        [
            ("title", talk["title"]),
            ("date", talk["date"]),
            ("authors", talk["authors"]),
            ("track", talk["track"]),
            ("short_description", talk["short_description"]),
            ("summary", talk["summary"]),
            ("weight", talk["weight"]),
        ],
        bare_keys={"date"},
    )
    body = textwrap.dedent(str(talk.get("body", ""))).strip()
    content = f"{front_matter}\n\n{body}\n" if body else f"{front_matter}\n\n"
    return PT_PRESENTATIONS / f"{slug}.md", content


def build_author_entry(author: dict[str, str]) -> tuple[Path, str]:
    front_matter = render_front_matter(
        [
            ("title", author["title"]),
            ("slug", author["slug"]),
            ("role", author["role"]),
            ("avatar", author["avatar"]),
        ]
    )
    bio = textwrap.dedent(author.get("bio", "")).strip()
    content = f"{front_matter}\n\n{bio}\n" if bio else f"{front_matter}\n\n"
    return PT_AUTHORS / f"{author['slug']}.md", content


def write_file(path: Path, content: str, *, force: bool, skip_if_exists: bool = False, dry_run: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if skip_if_exists and path.exists():
        print(f"[skip] {path.relative_to(ROOT)} already exists")
        return
    if path.exists() and not force:
        print(f"[skip] {path.relative_to(ROOT)} exists (use --force to overwrite)")
        return
    if dry_run:
        print(f"[dry-run] would write {path.relative_to(ROOT)}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"[write] {path.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Overwrite existing presentation files.")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without writing files.")
    args = parser.parse_args()

    for author in AUTHORS:
        path, content = build_author_entry(author)
        write_file(path, content, force=args.force, skip_if_exists=True, dry_run=args.dry_run)

    for talk in TALKS:
        path, content = build_presentation_entry(talk)
        write_file(path, content, force=args.force, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
