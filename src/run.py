# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "jinja2",
# ]
# ///

# Copyright (c) 2023 - 2025 Chair for Design Automation, TUM
# Copyright (c) 2025 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

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
    output_path: Path
    active: bool
    arguments: dict[str, str]


def main(
    *,
    synchronize_pull_request_template: bool,
    synchronize_security_policy: bool,
    package_url: str,
) -> None:
    """Render all templates."""
    template_containers = [
        TemplateContainer(
            file_name="pull_request_template.md",
            output_path=Path(".github"),
            active=synchronize_pull_request_template,
            arguments={},
        ),
        TemplateContainer(
            file_name="SECURITY.md",
            output_path=Path(".github"),
            active=synchronize_security_policy,
            arguments={"package_url": package_url},
        ),
    ]

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(Path(__file__).absolute().parent.parent / "templates"),
        autoescape=jinja2.select_autoescape(["html", "xml", "htm"]),
    )

    for template_container in template_containers:
        _render_template(environment, template_container)


def _render_template(environment: jinja2.Environment, template_container: TemplateContainer) -> None:
    """Render a single template."""
    if template_container.active:
        template = environment.get_template(template_container.file_name)
        output = template.render(**template_container.arguments)
        output_file = template_container.output_path / template_container.file_name
        output_file.write_text(output + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--synchronize_pull_request_template",
        default=True,
        type=bool,
        help="Whether to synchronize the pull-request template",
    )
    parser.add_argument(
        "--synchronize_security_policy",
        default=True,
        type=bool,
        help="Whether to synchronize the security policy",
    )
    parser.add_argument(
        "--package_url",
        type=str,
        required=True,
        help="GitHub URL of the MQT package",
    )
    args = parser.parse_args()

    main(
        synchronize_pull_request_template=args.synchronize_pull_request_template,
        synchronize_security_policy=args.synchronize_security_policy,
        package_url=args.package_url,
    )
