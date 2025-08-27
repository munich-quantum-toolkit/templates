# Copyright (c) 2023 - 2025 Chair for Design Automation, TUM
# Copyright (c) 2025 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "jinja2",
# ]
# ///

"""Python module for rendering templates."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import jinja2

DEFAULTS_DIR = Path(__file__).absolute().parent.parent / "defaults"
TEMPLATES_DIR = Path(__file__).absolute().parent.parent / "templates"


@dataclass
class TemplateContainer:
    """Container for template information."""

    file_name: str
    output_dir: Path
    active: bool
    arguments: dict[str, str] | None = None
    template_name: str | None = None

    def __post_init__(self) -> None:
        """Set the template name if not provided."""
        if self.template_name is None:
            self.template_name = self.file_name


def main(
    *,
    name: str,
    organization: str,
    project_type: str,
    repository: str,
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
    """Render all templates."""
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
            output_dir=Path(".github/CONTRIBUTING.md"),
            template_name="CONTRIBUTING.md",
            active=synchronize_contribution_guide,
            arguments={"name": name, "repository": repository},
        ),
        TemplateContainer(
            file_name="custom.css",
            output_dir=Path("docs/_static/custom.css"),
            active=synchronize_documentation_utilities,
            arguments=None,
        ),
        TemplateContainer(
            file_name="CONTRIBUTING.md",
            output_dir=Path("docs/CONTRIBUTING.md"),
            template_name="docs_contributing.md",
            active=synchronize_contribution_guide,
            arguments={
                "name": name,
                "organization": organization,
                "project_type": project_type,
                "repository": repository,
            },
        ),
        TemplateContainer(
            file_name="installation.md",
            output_dir=Path("docs/installation.md"),
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
            output_dir=Path("docs/lit_header.bib"),
            active=synchronize_documentation_utilities,
            arguments=None,
        ),
        TemplateContainer(
            file_name="page.html",
            output_dir=Path("docs/_templates/page.html"),
            active=synchronize_documentation_utilities,
            arguments=None,
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
            arguments=None,
        ),
        TemplateContainer(
            file_name="release-drafter.yml",
            template_name="release-drafter.yml.in",
            output_dir=Path(".github"),
            active=synchronize_release_drafter_template,
            arguments={"name": name, "release_drafter_categories": release_drafter_categories_dict},
        ),
        TemplateContainer(
            file_name="renovate.json5",
            output_dir=Path(".github"),
            active=synchronize_renovate_config,
            arguments=None,
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
        if template_container.arguments is None:
            _copy_template(template_container)
        else:
            _render_template(environment, template_container)


def _copy_template(template_container: TemplateContainer) -> None:
    """Copy a template without arguments."""
    if template_container.active:
        # Create output directory if it does not exist
        output_dir = template_container.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        # Read the template
        output = (TEMPLATES_DIR / template_container.file_name).read_text(encoding="utf-8")

        # Write the read template to a file
        output_path = output_dir / template_container.file_name
        output_path.write_text(output + "\n", encoding="utf-8")


def _render_template(environment: jinja2.Environment, template_container: TemplateContainer) -> None:
    """Render a template."""
    if template_container.active:
        # Create output directory if it does not exist
        output_dir = template_container.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        # Render the template
        template = environment.get_template(template_container.template_name)
        output = template.render(**template_container.arguments)

        # Write the rendered template to a file
        output_path = output_dir / template_container.file_name
        output_path.write_text(output + "\n", encoding="utf-8")


def _convert_to_bool(value: str) -> bool:
    if value in {"True", "true"}:
        return True
    if value in {"False", "false"}:
        return False
    msg = f"Invalid boolean value: {value}"
    raise ValueError(msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="Stylized name of the package (e.g., 'Core' or 'DDSIM')",
    )
    parser.add_argument(
        "--organization",
        type=str,
        required=True,
        help="Name of the repository's organization",
    )
    parser.add_argument(
        "--project_type",
        type=str,
        choices=["c++-python", "pure-python"],
        required=True,
        help="Type of the project",
    )
    parser.add_argument(
        "--repository",
        type=str,
        required=True,
        help="Name of the repository",
    )
    parser.add_argument(
        "--synchronize_contribution_guide",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize the contribution guide",
    )
    parser.add_argument(
        "--synchronize_documentation_utilities",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize documentation utilities such as page.html and custom.css",
    )
    parser.add_argument(
        "--synchronize_installation_guide",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize the installation guide",
    )
    parser.add_argument(
        "--synchronize_issue_templates",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize the issue templates",
    )
    parser.add_argument(
        "--synchronize_pull_request_template",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize the pull-request template",
    )
    parser.add_argument(
        "--synchronize_release_drafter_template",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize the Release Drafter template",
    )
    parser.add_argument(
        "--synchronize_renovate_config",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize the Renovate configuration",
    )
    parser.add_argument(
        "--synchronize_security_policy",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize the security policy",
    )
    parser.add_argument(
        "--synchronize_support_resources",
        default=True,
        type=_convert_to_bool,
        help="Whether to synchronize the support resources",
    )
    parser.add_argument(
        "--release_drafter_categories",
        type=str,
        default="",
        help="Release Drafter categories as a JSON string. If empty, a reasonable default will be used",
    )
    args = parser.parse_args()

    main(
        name=args.name,
        organization=args.organization,
        project_type=args.project_type,
        repository=args.repository,
        synchronize_contribution_guide=args.synchronize_contribution_guide,
        synchronize_documentation_utilities=args.synchronize_documentation_utilities,
        synchronize_installation_guide=args.synchronize_installation_guide,
        synchronize_issue_templates=args.synchronize_issue_templates,
        synchronize_pull_request_template=args.synchronize_pull_request_template,
        synchronize_release_drafter_template=args.synchronize_release_drafter_template,
        synchronize_renovate_config=args.synchronize_renovate_config,
        synchronize_security_policy=args.synchronize_security_policy,
        synchronize_support_resources=args.synchronize_support_resources,
        release_drafter_categories=args.release_drafter_categories,
    )
