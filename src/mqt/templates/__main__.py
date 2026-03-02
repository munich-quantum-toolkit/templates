# Copyright (c) 2025 - 2026 Chair for Design Automation, TUM
# Copyright (c) 2025 - 2026 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""Main entry point for rendering templates."""

from __future__ import annotations

import argparse
from pathlib import Path

from .render_templates import render_templates


def _convert_to_bool(value: str) -> bool:
    if value in {"True", "true"}:
        return True
    if value in {"False", "false"}:
        return False
    msg = f"Invalid boolean value: {value}"
    raise ValueError(msg)


def main() -> None:
    """Parse arguments and render templates."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target_dir",
        type=str,
        default=".",
        help="Target directory for the rendered templates",
    )
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
        choices=["c++-python", "c++-mlir-python", "pure-python", "other"],
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
        "--has_changelog_and_upgrade_guide",
        default=True,
        type=_convert_to_bool,
        help="Whether the repository has a changelog and upgrade guide",
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

    render_templates(
        target_dir=Path(args.target_dir),
        name=args.name,
        organization=args.organization,
        project_type=args.project_type,
        repository=args.repository,
        has_changelog_and_upgrade_guide=args.has_changelog_and_upgrade_guide,
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


if __name__ == "__main__":
    main()
