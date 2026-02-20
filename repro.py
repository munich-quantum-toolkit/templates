import jinja2
from pathlib import Path

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
Path("repro_tooling.md").write_text(output)
print("Rendered to repro_tooling.md")
