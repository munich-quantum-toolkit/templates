# Copyright (c) 2025 - 2026 Chair for Design Automation, TUM
# Copyright (c) 2025 - 2026 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""Python module for rendering templates."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import jinja2

DEFAULTS_DIR = Path(__file__).absolute().parent.parent.parent.parent / "defaults"
TEMPLATES_DIR = Path(__file__).absolute().parent.parent.parent.parent / "templates"
ROOT_DIR = Path().absolute()


@dataclass
class TemplateContainer:
    """Container for template information."""

    file_name: str
    output_dir: Path
    active: bool
    arguments: dict[str, str | bool] | None = None
    template_name: str | None = None

    def __post_init__(self) -> None:
        """Set the template name if not provided."""
        if self.template_name is None:
            self.template_name = self.file_name


def render_templates(
    *,
    target_dir: Path,
    name: str,
    organization: str,
    project_type: str,
    repository: str,
    has_changelog_and_upgrade_guide: bool,
    synchronize_contribution_guide: bool,
    synchronize_documentation_utilities: bool,
    synchronize_installation_guide: bool,
    synchronize_issue_templates: bool,
    synchronize_pull_request_template: bool,
    synchronize_release_drafter_template: bool,
    synchronize_renovate_config: bool,
    synchronize_security_policy: bool,
    synchronize_support_resources: bool,
    release_drafter_categories: str,
) -> None:
    """Render templates.

    Raises:
        ValueError: If the arguments are incompatible with each other.
    """
    if project_type == "other":
        if synchronize_contribution_guide:
            msg = "Contribution guide cannot be synchronized for project type 'other'."
            raise ValueError(msg)
        if synchronize_installation_guide:
            msg = "Installation guide cannot be synchronized for project type 'other'."
            raise ValueError(msg)

    if not release_drafter_categories:
        release_drafter_categories = Path(DEFAULTS_DIR / "release_drafter_categories.json").read_text(encoding="utf-8")
    release_drafter_categories_dict = json.loads(release_drafter_categories)

    template_containers = [
        TemplateContainer(
            file_name="bug-report.yml",
            output_dir=Path(".github/ISSUE_TEMPLATE"),
            active=synchronize_issue_templates,
            arguments={"name": name, "organization": organization, "repository": repository},
        ),
        TemplateContainer(
            file_name="CONTRIBUTING.md",
            output_dir=Path(".github"),
            active=synchronize_contribution_guide,
            arguments={"name": name, "repository": repository},
        ),
        TemplateContainer(
            file_name="custom.css",
            output_dir=Path("docs/_static"),
            active=synchronize_documentation_utilities,
        ),
        TemplateContainer(
            template_name="docs_contributing.md",
            file_name="contributing.md",
            output_dir=Path("docs"),
            active=synchronize_contribution_guide,
            arguments={
                "name": name,
                "organization": organization,
                "project_type": project_type,
                "repository": repository,
                "has_changelog_and_upgrade_guide": has_changelog_and_upgrade_guide,
            },
        ),
        TemplateContainer(
            template_name="docs_support.md",
            file_name="support.md",
            output_dir=Path("docs"),
            active=synchronize_documentation_utilities,
        ),
        TemplateContainer(
            file_name="installation.md",
            output_dir=Path("docs"),
            active=synchronize_installation_guide,
            arguments={
                "name": name,
                "organization": organization,
                "project_type": project_type,
                "repository": repository,
            },
        ),
        TemplateContainer(
            file_name="lit_header.bib",
            output_dir=Path("docs"),
            active=synchronize_documentation_utilities,
        ),
        TemplateContainer(
            file_name="page.html",
            output_dir=Path("docs/_templates"),
            active=synchronize_documentation_utilities,
        ),
        TemplateContainer(
            file_name="feature-request.yml",
            output_dir=Path(".github/ISSUE_TEMPLATE"),
            active=synchronize_issue_templates,
            arguments={"organization": organization, "repository": repository},
        ),
        TemplateContainer(
            file_name="pull_request_template.md",
            output_dir=Path(".github"),
            active=synchronize_pull_request_template,
            arguments={"has_changelog_and_upgrade_guide": has_changelog_and_upgrade_guide},
        ),
        TemplateContainer(
            template_name="release-drafter.yml.in",
            file_name="release-drafter.yml",
            output_dir=Path(".github"),
            active=synchronize_release_drafter_template,
            arguments={
                "name": name,
                "release_drafter_categories": release_drafter_categories_dict,
                "has_changelog_and_upgrade_guide": has_changelog_and_upgrade_guide,
            },
        ),
        TemplateContainer(
            file_name="renovate.json5",
            output_dir=Path(".github"),
            active=synchronize_renovate_config,
        ),
        TemplateContainer(
            file_name="SECURITY.md",
            output_dir=Path(".github"),
            active=synchronize_security_policy,
            arguments={"organization": organization, "repository": repository},
        ),
        TemplateContainer(
            file_name="SUPPORT.md",
            output_dir=Path(".github"),
            active=synchronize_support_resources,
            arguments={"name": name, "organization": organization, "repository": repository},
        ),
    ]

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_DIR),
        autoescape=jinja2.select_autoescape(["html", "xml", "htm"]),
    )

    for template_container in template_containers:
        output_dir = target_dir / template_container.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        if template_container.arguments is None:
            _copy_template(template_container, output_dir)
        else:
            _render_template(environment, template_container, output_dir)


def _copy_template(template_container: TemplateContainer, output_dir: Path) -> None:
    """Copy a template without arguments."""
    if template_container.active:
        assert template_container.template_name is not None

        # Read the template
        output = (TEMPLATES_DIR / template_container.template_name).read_text(encoding="utf-8")

        # Write the read template to a file
        output_path = output_dir / template_container.file_name
        output_path.write_text(output, encoding="utf-8")


def _render_template(environment: jinja2.Environment, template_container: TemplateContainer, output_dir: Path) -> None:
    """Render a template."""
    if template_container.active:
        assert template_container.arguments is not None
        assert template_container.template_name is not None

        # Render the template
        template = environment.get_template(template_container.template_name)
        output = template.render(**template_container.arguments)

        # Write the rendered template to a file
        output_path = output_dir / template_container.file_name
        output_path.write_text(output + "\n", encoding="utf-8")
