#!/usr/bin/env python3
"""
Build script per generar .skill files (ZIP) per la Tana Paste Generator skill.

Usage: python scripts/build_skill.py [--version X.Y.Z]
"""

import zipfile
import os
import sys
import re
from pathlib import Path
from datetime import datetime

# Configuracio
SKILL_NAME = "tana-paste"
SKILL_DIR = Path(__file__).parent.parent  # tana-paste/
OUTPUT_DIR = SKILL_DIR / "dist"
VERSION_FILE = SKILL_DIR / "VERSION"


def get_version():
    """Obte la versio del skill."""
    # Prioritat: argument CLI > VERSION file > CHANGELOG > default
    if len(sys.argv) > 2 and sys.argv[1] == "--version":
        return sys.argv[2]

    if VERSION_FILE.exists():
        return VERSION_FILE.read_text().strip()

    # Intentar extreure de CHANGELOG.md
    changelog = SKILL_DIR / "CHANGELOG.md"
    if changelog.exists():
        content = changelog.read_text()
        match = re.search(r"## \[?v?(\d+\.\d+(?:\.\d+)?)\]?", content)
        if match:
            return match.group(1)

    return "1.0.0"


def validate_skill():
    """Valida que l'estructura del skill sigui correcta."""
    skill_md = SKILL_DIR / "SKILL.md"

    if not skill_md.exists():
        raise FileNotFoundError(f"SKILL.md no trobat a {SKILL_DIR}")

    content = skill_md.read_text(encoding="utf-8")

    # Validar frontmatter YAML
    if not content.startswith("---"):
        raise ValueError("SKILL.md ha de comencar amb frontmatter YAML (---)")

    # Validar camps obligatoris
    if "name:" not in content:
        raise ValueError("SKILL.md ha de tenir camp 'name' al frontmatter")
    if "description:" not in content:
        raise ValueError("SKILL.md ha de tenir camp 'description' al frontmatter")

    print(f"✓ Validacio correcta: {skill_md}")


def build_skill(version: str):
    """Genera el fitxer .skill (ZIP)."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    output_file = OUTPUT_DIR / f"{SKILL_NAME}-v{version}.skill"

    # Fitxers a incloure
    include_patterns = [
        "SKILL.md",
        "README.md",
        "CHANGELOG.md",
        "VERSION",
        "reference.md",
        "examples/**/*.md",
    ]

    # Fitxers a excloure
    exclude_patterns = [
        "scripts/",
        "dist/",
        ".git/",
        "__pycache__/",
        "*.pyc",
        ".DS_Store",
    ]

    files_to_add = []

    for pattern in include_patterns:
        if "**" in pattern:
            # Glob recursiu
            for file_path in SKILL_DIR.glob(pattern):
                if file_path.is_file():
                    files_to_add.append(file_path)
        else:
            file_path = SKILL_DIR / pattern
            if file_path.exists() and file_path.is_file():
                files_to_add.append(file_path)

    # Crear ZIP
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(set(files_to_add)):
            # Check exclusions
            skip = False
            for exclude in exclude_patterns:
                if exclude.rstrip("/") in str(file_path):
                    skip = True
                    break

            if skip:
                continue

            arcname = str(file_path.relative_to(SKILL_DIR))
            zf.write(file_path, arcname)
            print(f"  + {arcname}")

    print(f"\n✓ Generat: {output_file}")
    print(f"  Mida: {output_file.stat().st_size:,} bytes")

    return output_file


def main():
    print(f"=== Build Skill: {SKILL_NAME} ===\n")

    try:
        validate_skill()
        version = get_version()
        print(f"\nVersio: {version}")
        print(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

        output = build_skill(version)

        print(f"\n=== BUILD COMPLETAT ===")
        print(f"\nPer distribuir:")
        print(f"  1. claude.ai: Settings > Capabilities > Upload {output.name}")
        print(f"  2. GitHub: Crear Release i adjuntar {output.name}")
        print(f"  3. Claude Code: Ja disponible automaticament a ~/.claude/skills/")

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
