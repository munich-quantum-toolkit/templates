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
from dataclasses import dataclass
from pathlib import Path

import jinja2


@dataclass
class TemplateContainer:
    """Container for template information."""

    file_name: str
    output_dir: Path
    active: bool
    arguments: dict[str, str]


def main(
    *,
    organization: str,
    repository: str,
    name: str,
    synchronize_issue_templates: bool,
    synchronize_pull_request_template: bool,
    synchronize_security_policy: bool,
    synchronize_support_resources: bool,
) -> None:
    """Render all templates."""
    template_containers = [
        TemplateContainer(
            file_name="bug-report.yml",
            output_dir=Path(".github/ISSUE_TEMPLATE"),
            active=synchronize_issue_templates,
            arguments={"organization": organization, "repository": repository, "name": name},
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
            arguments={},
        ),
        TemplateContainer(
            file_name="SECURITY.md",
            output_dir=Path(".github"),
            active=synchronize_security_policy,
            arguments={"organization": organization, "repository": repository},
        ),
        TemplateContainer(
            file_name="support.md",
            output_dir=Path(".github"),
            active=synchronize_support_resources,
            arguments={"organization": organization, "repository": repository, "name": name},
        ),
    ]

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(Path(__file__).absolute().parent.parent / "templates"),
        autoescape=jinja2.select_autoescape(["html", "xml", "htm"]),
    )

    for template_container in template_containers:
        _render_template(environment, template_container)


def _render_template(environment: jinja2.Environment, template_container: TemplateContainer) -> None:
    """Render a template."""
    if template_container.active:
        template = environment.get_template(template_container.file_name)
        output = template.render(**template_container.arguments)
        output_path = template_container.output_dir / template_container.file_name
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
        "--organization",
        type=str,
        required=True,
        help="Name of the repository's organization",
    )
    parser.add_argument(
        "--repository",
        type=str,
        required=True,
        help="Name of the repository",
    )
    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="Stylized name of the package (e.g., 'Core' or 'DDSIM')",
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
    args = parser.parse_args()

    main(
        organization=args.organization,
        repository=args.repository,
        name=args.name,
        synchronize_issue_templates=args.synchronize_issue_templates,
        synchronize_pull_request_template=args.synchronize_pull_request_template,
        synchronize_security_policy=args.synchronize_security_policy,
        synchronize_support_resources=args.synchronize_support_resources,
    )
