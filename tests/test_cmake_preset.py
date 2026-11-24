# Copyright (c) 2025 - 2026 Chair for Design Automation, TUM
# Copyright (c) 2025 - 2026 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""Test dependency extraction from annotated CMake release versions."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest


@pytest.mark.parametrize(("dep_name", "version"), [("aws/aws-sdk-cpp", "1.11.935"), ("nlohmann/json", "v3.12.0")])
@pytest.mark.parametrize("quote", ["", '"'])
def test_release_versions(dep_name: str, version: str, quote: str) -> None:
    """Extract full release versions with and without a tag prefix or quotes."""
    preset = json.loads((Path(__file__).parents[1] / "renovate/cmake.json").read_text())
    pattern = preset["customManagers"][0]["matchStrings"][1]
    content = f"# renovate: datasource=github-releases depName={dep_name}\nset(VERSION {quote}{version}{quote})\n"

    # Python uses a different spelling for JavaScript's named capture groups.
    match = re.search(pattern.replace("(?<", "(?P<"), content)

    assert match is not None
    assert match.groupdict() == {"datasource": "github-releases", "depName": dep_name, "currentValue": version}
