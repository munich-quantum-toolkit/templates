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
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import jinja2

TEMPLATES_DIR = Path(".templates")


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
    organization: str,
    repository: str,
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
            arguments={"organization": organization, "repository": repository},
        ),
    ]

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(Path(__file__).absolute().parent.parent / "templates"),
        autoescape=jinja2.select_autoescape(["html", "xml", "htm"]),
    )

    TEMPLATES_DIR.mkdir(parents=False, exist_ok=True)

    with tempfile.TemporaryDirectory() as old_templates_dir_str:
        old_templates_dir = Path(old_templates_dir_str)
        for template_container in template_containers:
            _get_old_template(template_container, old_templates_dir)
            _render_template(environment, template_container)
            _write_target_file(template_container, old_templates_dir)


def _get_old_template(template_container: TemplateContainer, old_templates_dir: Path) -> None:
    """Get the previous version of the rendered template from the ``main`` branch."""
    if template_container.active:
        output_file = old_templates_dir / template_container.file_name
        with output_file.open("w", encoding="utf-8") as f:
            command = [
                "git",
                "show",
                f"main:.templates/{template_container.file_name}",
            ]
            try:
                subprocess.run(command, stdout=f, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Warning: Failed to retrieve old template for {template_container.file_name}. Error: {e}")
                f.write("")  # Write an empty file to ensure downstream processes can proceed


def _render_template(environment: jinja2.Environment, template_container: TemplateContainer) -> None:
    """Render a template."""
    if template_container.active:
        template = environment.get_template(template_container.file_name)
        output = template.render(**template_container.arguments)
        output_file = TEMPLATES_DIR / template_container.file_name
        output_file.write_text(output + "\n", encoding="utf-8")


def _write_target_file(template_container: TemplateContainer, old_templates_dir: Path) -> None:
    """Write the target file using ``git merge-file``."""
    if template_container.active:
        target_file = template_container.output_path / template_container.file_name
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.touch(exist_ok=True)

        old_template = old_templates_dir / template_container.file_name
        new_template = TEMPLATES_DIR / template_container.file_name

        command = [
            "git",
            "merge-file",
            str(target_file),
            str(old_template),
            str(new_template),
        ]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to merge files for {template_container.file_name}. Error: {e}")


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
    args = parser.parse_args()

    main(
        synchronize_pull_request_template=args.synchronize_pull_request_template,
        synchronize_security_policy=args.synchronize_security_policy,
        organization=args.organization,
        repository=args.repository,
    )
