#!/usr/bin/env python3

import os
import re

docs_dir = "assets/docs"
files = sorted(os.listdir(docs_dir))

cover = files[0]
sections = files[1:]

toc_lines: list[str] = []
for filename in sections:
    filepath = os.path.join(docs_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
    title = first_line.lstrip("#").strip()
    anchor = re.sub(r"[^\w\s-]", "", title.lower()).strip().replace(" ", "-")
    toc_lines.append(f"- [{title}](#{anchor})")

toc: str = "## Contenido\n" + "\n".join(toc_lines) + "\n\n---\n\n"

with open("README.md", "w", encoding="utf-8") as readme:
    # Primero la portada
    with open(os.path.join(docs_dir, cover), "r", encoding="utf-8") as f:
        readme.write(f.read())
        readme.write("\n\n---\n\n")
    # Luego el índice
    readme.write(toc)
    # Luego el resto
    for filename in sections:
        filepath = os.path.join(docs_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            readme.write(f.read())
            readme.write("\n\n---\n\n")

print("README.md generado")
