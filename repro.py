# Copyright (c) 2025 - 2026 Chair for Design Automation, TUM
# Copyright (c) 2025 - 2026 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

from pathlib import Path

import jinja2

TEMPLATES_DIR = Path("templates")
render_args = {
    "name": "Test",
    "organization": "munich-quantum-toolkit",
    "project_type": "c++-python",
    "repository": "test",
    "has_changelog_and_upgrade_guide": True,
}

env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))
template = env.get_template("docs_tooling.md")
output = template.render(**render_args)
Path("repro_tooling.md").write_text(output, encoding="utf-8")
print("Rendered to repro_tooling.md")
