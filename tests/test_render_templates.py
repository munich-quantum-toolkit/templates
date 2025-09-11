# Copyright (c) 2023 - 2025 Chair for Design Automation, TUM
# Copyright (c) 2025 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""Test the render_templates() function."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from mqt.templates.render_templates import render_templates

if TYPE_CHECKING:
    from collections.abc import Generator

    from pytest_mock import MockFixture


@pytest.fixture
def temp_dir(mocker: MockFixture) -> Generator[Path]:
    """Create a temporary directory for testing.

    Yields:
        The path to the temporary directory.
    """
    temp_dir = Path(__file__).absolute().parent.parent / "temp"
    temp_dir.mkdir(exist_ok=True)
    mocker.patch("mqt.templates.render_templates.ROOT_DIR", temp_dir)
    yield temp_dir
    shutil.rmtree(temp_dir)


def _check_files(files: list[Path]) -> None:
    for file in files:
        assert file.exists()
        file_before = file.read_text()
        subprocess.run(["pre-commit", "run", "--show-diff-on-failure", "--files", file], check=False)
        file_after = file.read_text()
        assert file_before == file_after, f"File {file.name} was modified by pre-commit"


def test_cpp_python(temp_dir: Path) -> None:
    """Test that templates for `c++-python` projects are rendered correctly."""
    render_templates(
        name="Test",
        organization="munich-quantum-toolkit",
        project_type="c++-python",
        repository="test",
        has_changelog_and_upgrade_guide=True,
        synchronize_contribution_guide=True,
        synchronize_documentation_utilities=True,
        synchronize_installation_guide=True,
        synchronize_issue_templates=True,
        synchronize_pull_request_template=True,
        synchronize_release_drafter_template=True,
        synchronize_renovate_config=True,
        synchronize_security_policy=True,
        synchronize_support_resources=True,
        release_drafter_categories="",
    )

    files = [
        temp_dir / ".github" / "CONTRIBUTING.md",
        temp_dir / ".github" / "ISSUE_TEMPLATE" / "bug-report.yml",
        temp_dir / ".github" / "ISSUE_TEMPLATE" / "feature-request.yml",
        temp_dir / ".github" / "pull_request_template.md",
        temp_dir / ".github" / "release-drafter.yml",
        temp_dir / ".github" / "renovate.json5",
        temp_dir / ".github" / "SECURITY.md",
        temp_dir / ".github" / "SUPPORT.md",
        temp_dir / "docs" / "_static" / "custom.css",
        temp_dir / "docs" / "_templates" / "page.html",
        temp_dir / "docs" / "contributing.md",
        temp_dir / "docs" / "installation.md",
        temp_dir / "docs" / "lit_header.bib",
    ]
    _check_files(files)


def test_pure_python(temp_dir: Path) -> None:
    """Test that templates for `pure-python` projects are rendered correctly."""
    render_templates(
        name="Test",
        organization="munich-quantum-toolkit",
        project_type="pure-python",
        repository="test",
        has_changelog_and_upgrade_guide=True,
        synchronize_contribution_guide=True,
        synchronize_documentation_utilities=True,
        synchronize_installation_guide=True,
        synchronize_issue_templates=True,
        synchronize_pull_request_template=True,
        synchronize_release_drafter_template=True,
        synchronize_renovate_config=True,
        synchronize_security_policy=True,
        synchronize_support_resources=True,
        release_drafter_categories="",
    )

    files = [
        temp_dir / ".github" / "CONTRIBUTING.md",
        temp_dir / ".github" / "ISSUE_TEMPLATE" / "bug-report.yml",
        temp_dir / ".github" / "ISSUE_TEMPLATE" / "feature-request.yml",
        temp_dir / ".github" / "pull_request_template.md",
        temp_dir / ".github" / "release-drafter.yml",
        temp_dir / ".github" / "renovate.json5",
        temp_dir / ".github" / "SECURITY.md",
        temp_dir / ".github" / "SUPPORT.md",
        temp_dir / "docs" / "_static" / "custom.css",
        temp_dir / "docs" / "_templates" / "page.html",
        temp_dir / "docs" / "contributing.md",
        temp_dir / "docs" / "installation.md",
        temp_dir / "docs" / "lit_header.bib",
    ]
    _check_files(files)


def test_other(temp_dir: Path) -> None:
    """Test that templates for `other` projects are rendered correctly."""
    render_templates(
        name="Test",
        organization="munich-quantum-toolkit",
        project_type="other",
        repository="test",
        has_changelog_and_upgrade_guide=True,
        synchronize_contribution_guide=False,
        synchronize_documentation_utilities=True,
        synchronize_installation_guide=False,
        synchronize_issue_templates=True,
        synchronize_pull_request_template=True,
        synchronize_release_drafter_template=True,
        synchronize_renovate_config=True,
        synchronize_security_policy=True,
        synchronize_support_resources=True,
        release_drafter_categories="",
    )

    files = [
        temp_dir / ".github" / "ISSUE_TEMPLATE" / "bug-report.yml",
        temp_dir / ".github" / "ISSUE_TEMPLATE" / "feature-request.yml",
        temp_dir / ".github" / "pull_request_template.md",
        temp_dir / ".github" / "release-drafter.yml",
        temp_dir / ".github" / "renovate.json5",
        temp_dir / ".github" / "SECURITY.md",
        temp_dir / ".github" / "SUPPORT.md",
        temp_dir / "docs" / "_static" / "custom.css",
        temp_dir / "docs" / "_templates" / "page.html",
        temp_dir / "docs" / "lit_header.bib",
    ]
    _check_files(files)
