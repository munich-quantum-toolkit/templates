<!--- This file has been generated from an external template. Please do not modify it directly. -->
<!--- Changes should be contributed to https://github.com/munich-quantum-toolkit/templates. -->

{%- if project_type == "c++-python" %}

# Installation

MQT {{name}} is primarily developed as a C++20 library with Python bindings.
The Python package is available on [PyPI](https://pypi.org/project/mqt.{{repository}}/) and can be installed on all major operating systems with all [officially supported Python versions](https://devguide.python.org/versions/).

{%- elif project_type == "pure-python" %}

# Installation

MQT {{name}} is a Python package available on [PyPI](https://pypi.org/project/mqt.{{repository}}/).
It can be installed on all major operating systems with all [officially supported Python versions](https://devguide.python.org/versions/).

{%- endif %}

:::::{tip}
:name: uv-recommendation

We recommend using [{code}`uv`][uv].
It is a fast Python package and project manager by [Astral](https://astral.sh/) (creators of [{code}`ruff`][ruff]).
It can replace {code}`pip` and {code}`virtualenv`, automatically manages virtual environments, installs packages, and can install Python itself.
It is significantly faster than {code}`pip`.

If you do not have {code}`uv` installed, install it with:

::::{tab-set}
:::{tab-item} macOS and Linux

```console
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

:::
:::{tab-item} Windows

```console
$ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

:::
::::

See the [uv documentation][uv] for more information.

:::::

::::{tab-set}
:sync-group: installer

:::{tab-item} {code}`uv` _(recommended)_
:sync: uv

```console
$ uv pip install mqt.{{repository}}
```

:::

:::{tab-item} {code}`pip`
:sync: pip

```console
(.venv) $ python -m pip install mqt.{{repository}}
```

:::
::::

{%- if project_type == "c++-python" %}
In most cases, no compilation is required; a platform-specific prebuilt wheel is downloaded and installed.
{%- endif %}

Verify the installation:

```console
(.venv) $ python -c "import mqt.{{repository}}; print(mqt.{{repository}}.__version__)"
```

This prints the installed package version.

{%- if project_type == "c++-python" %}

## Building from Source for Performance

To get the best performance and enable platform-specific optimizations not available in portable wheels, we recommend building the library from source:

::::{tab-set}
:sync-group: installer

:::{tab-item} {code}`uv` _(recommended)_
:sync: uv

```console
$ uv pip install mqt.{{repository}} --no-binary mqt.{{repository}}
```

:::

:::{tab-item} {code}`pip`
:sync: pip

```console
(.venv) $ pip install mqt.{{repository}} --no-binary mqt.{{repository}}
```

:::
::::
This requires a C++20-capable [C++ compiler](https://en.wikipedia.org/wiki/List_of_compilers#C++_compilers) and [CMake](https://cmake.org/) 3.24 or newer.

{%- if has_mlir %}

## Setting Up MLIR

MQT {{name}} enables [MLIR](https://mlir.llvm.org/) by default for building from source ([📦️ Enable MLIR by default — #1356](https://github.com/munich-quantum-toolkit/core/pull/1356)).
MLIR is part of the [LLVM](https://llvm.org/) project and provides the intermediate representation used by MQT {{name}} for quantum programs.
To build from source, you must install MLIR and make it available to both the C++ and Python builds on your platform.

The recommended approach is to use the [`setup-mlir`](https://github.com/munich-quantum-software/setup-mlir/) scripts to download a pre-built MLIR distribution; the binaries are produced by the [portable-mlir-toolchain](https://github.com/munich-quantum-software/portable-mlir-toolchain/) project.

### Downloading the MLIR Distribution

The [`setup-mlir`](https://github.com/munich-quantum-software/setup-mlir/) repository provides installation scripts for all supported operating systems.
You must pass the LLVM version (e.g., `21.1.8`) and the installation prefix (directory) where MLIR should be extracted.
The scripts download a platform-specific archive and use an embedded `zstd` helper for decompression, so the only host requirement is `tar`.

::::{note}
:name: tar-requirement

`tar` is included by default on Windows 10 and Windows 11.
On older Windows versions, install it for example via [Chocolatey](https://chocolatey.org/): `choco install tar`.
::::

::::{tab-set}
:::{tab-item} macOS and Linux

Run the Bash script with the desired LLVM version and installation path:

```console
$ curl -LsSf https://github.com/munich-quantum-software/setup-mlir/releases/latest/download/setup-mlir.sh | bash -s -- -v 21.1.8 -p /path/to/installation
```

Replace `/path/to/installation` with the directory where MLIR should be installed (e.g., `$HOME/mlir` or `/opt/mlir`).

:::
:::{tab-item} Windows

Run the PowerShell script with the desired LLVM version and installation path:

```console
$ powershell -ExecutionPolicy ByPass -c "& ([scriptblock]::Create((irm https://github.com/munich-quantum-software/setup-mlir/releases/latest/download/setup-mlir.ps1))) -llvm_version 21.1.8 -install_prefix C:\path\to\installation"
```

Replace `C:\path\to\installation` with the directory where MLIR should be installed (e.g., `C:\mlir`).
For debug builds on Windows, add the `-use_debug` flag to the script invocation.

:::
::::

For supported LLVM versions, commit hashes, and other options, see the [`setup-mlir`](https://github.com/munich-quantum-software/setup-mlir/) repository and its [version-manifest.json](https://github.com/munich-quantum-software/setup-mlir/blob/main/version-manifest.json).

### Making MLIR Available to the Build

After installing MLIR, point the build system to it by setting the CMake variable {code}`MLIR_DIR` to the **CMake configuration directory** of the installation: {code}`<install-prefix>/lib/cmake/mlir`.
Use the same prefix you passed to the setup script (e.g., {code}`/path/to/installation` or {code}`C:\path\to\installation`).

::::{tab-set}

:::{tab-item} C++ Build

Pass {code}`MLIR_DIR` when configuring with CMake:

::::{tab-set}
:::{tab-item} macOS and Linux

```console
$ cmake -S . -B build -DMLIR_DIR=/path/to/installation/lib/cmake/mlir
```

:::
:::{tab-item} Windows

```console
$ cmake -S . -B build -DMLIR_DIR=C:/path/to/installation/lib/cmake/mlir
```

Use forward slashes in the path, or escape backslashes when passing the value to CMake.

:::
::::

:::

:::{tab-item} Python Build

When building the Python package from source, set {code}`MLIR_DIR` via the {code}`CMAKE_ARGS` environment variable so that the build backend passes it to CMake:

::::{tab-set}
:::{tab-item} macOS and Linux

```console
(.venv) $ CMAKE_ARGS="-DMLIR_DIR=/path/to/installation/lib/cmake/mlir" pip install .
```

:::
:::{tab-item} Windows

```console
(.venv) $ $env:CMAKE_ARGS="-DMLIR_DIR=C:/path/to/installation/lib/cmake/mlir"; pip install .
```

:::
::::

:::

::::

### Using CMake Presets

In addition to passing {code}`MLIR_DIR` on the command line, you can use [CMake Presets](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html) so that common scenarios (e.g., a fixed MLIR install path) are configured once. The project may ship a {code}`CMakePresets.json` with presets for common scenarios; you can also add your own preset as shown below.

Define a preset that sets {code}`MLIR_DIR` in {code}`cacheVariables`; then configure with {code}`--preset default` (or your preset name) and build as usual.

Example preset that uses a local MLIR installation:

```json
{
  "version": 3,
  "configurePresets": [
    {
      "name": "default",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/build",
      "cacheVariables": {
        "MLIR_DIR": "/path/to/installation/lib/cmake/mlir"
      }
    }
  ]
}
```

On Windows, use a path with forward slashes (e.g., {code}`C:/mlir/lib/cmake/mlir`).
After adding or updating presets in {code}`CMakePresets.json` in the project root, run:

```console
$ cmake --preset default
$ cmake --build build
```

For Python builds, set {code}`CMAKE_ARGS` to include {code}`-DMLIR_DIR=...` as shown above, or use a preset that is applied when the Python build invokes CMake, if your workflow supports it.

### Disabling MLIR

If you do not need MLIR-based functionality, you can disable it by setting the {code}`BUILD_MQT_{{name.upper()}}_MLIR` option to {code}`OFF`.
This disables all MLIR-related features in MQT {{name}}.

```console
$ cmake -S . -B build -DBUILD_MQT_{{name.upper()}}_MLIR=OFF
```

{%- endif %}

{%- endif %}

## Integrating MQT {{name}} into Your Project

To use the MQT {{name}} Python package in your project, add it as a dependency in your {code}`pyproject.toml` or {code}`setup.py`.
This ensures the package is installed when your project is installed.

::::{tab-set}

:::{tab-item} {code}`uv` _(recommended)_

```console
$ uv add mqt.{{repository}}
```

:::

:::{tab-item} {code}`pyproject.toml`

```toml
[project]
# ...
dependencies = ["mqt.{{repository}}>=<version>"]
# ...
```

:::

:::{tab-item} {code}`setup.py`

```python
from setuptools import setup

setup(
    # ...
    install_requires=["mqt.{{repository}}>=<version>"],
    # ...
)
```

:::
::::

{%- if project_type == "c++-python" %}

If you want to integrate the C++ library directly into your project, you can either

- add it as a [{code}`git` submodule][git-submodule] and build it as part of your project, or
- install MQT {{name}} on your system and use CMake's {code}`find_package()` command to locate it, or
- use CMake's [{code}`FetchContent`][FetchContent] module to combine both approaches.

::::{tab-set}
:::{tab-item} {code}`FetchContent`

This is the recommended approach because it lets you detect installed versions of MQT {{name}} and only downloads the library if it is not available on the system.
Furthermore, CMake's [{code}`FetchContent`][FetchContent] module provides flexibility in how the library is integrated into the project.

```cmake
include(FetchContent)
set(FETCH_PACKAGES "")

# cmake-format: off
set(MQT_{{name.upper()}}_MINIMUM_VERSION "<minimum_version>"
    CACHE STRING "MQT {{name}} minimum version")
set(MQT_{{name.upper()}}_VERSION "<version>"
    CACHE STRING "MQT {{name}} version")
set(MQT_{{name.upper()}}_REV "<revision>"
    CACHE STRING "MQT {{name}} identifier (tag, branch or commit hash)")
set(MQT_{{name.upper()}}_REPO_OWNER "{{organization}}"
    CACHE STRING "MQT {{name}} repository owner (change when using a fork)")
# cmake-format: on
FetchContent_Declare(
  mqt-{{repository}}
  GIT_REPOSITORY https://github.com/${MQT_{{name.upper()}}_REPO_OWNER}/{{repository}}.git
  GIT_TAG ${MQT_{{name.upper()}}_REV}
  FIND_PACKAGE_ARGS ${MQT_{{name.upper()}}_MINIMUM_VERSION})
list(APPEND FETCH_PACKAGES mqt-{{repository}})

# Make all declared dependencies available.
FetchContent_MakeAvailable(${FETCH_PACKAGES})
```

:::

:::{tab-item} {code}`git-submodule`

Adding the library as a [{code}`git` submodule][git-submodule] is a simple approach.
However, {code}`git` submodules can be cumbersome, especially when working with multiple branches or versions of the library.
First, add the submodule to your project (e.g., in the {code}`external` directory):

```console
$ git submodule add https://github.com/{{organization}}/{{repository}}.git external/mqt-{{repository}}
```

Then add the following line to your {code}`CMakeLists.txt` to make the library's targets available in your project:

```cmake
add_subdirectory(external/mqt-{{repository}})
```

:::

:::{tab-item} {code}`find_package()`

You can install MQT {{name}} on your system after building it from source:

```console
$ git clone https://github.com/{{organization}}/{{repository}}.git mqt-{{repository}}
$ cd mqt-{{repository}}
$ cmake -S . -B build
$ cmake --build build
$ cmake --install build
```

Then, in your project's {code}`CMakeLists.txt`, use {code}`find_package()` to locate the installed library:

```cmake
find_package(mqt-{{repository}} <version> REQUIRED)
```

:::

::::

{%- endif %}

(development-setup)=

## Development Setup

Set up a reproducible development environment for MQT {{name}}.
This is the recommended starting point for both bug fixes and new features.
For detailed guidelines and workflows, see {doc}`contributing`.

1.  Get the code:

    ::::{tab-set}
    :::{tab-item} External Contribution
    If you do not have write access to the [{{organization}}/{{repository}}](https://github.com/{{organization}}/{{repository}}) repository, fork the repository on GitHub (see <https://docs.github.com/en/get-started/quickstart/fork-a-repo>) and clone your fork locally.

    ```console
    $ git clone git@github.com:your_name_here/{{repository}}.git mqt-{{repository}}
    ```

    :::
    :::{tab-item} Internal Contribution
    If you have write access to the [{{organization}}/{{repository}}](https://github.com/{{organization}}/{{repository}}) repository, clone the repository locally.

    ```console
    $ git clone git@github.com/{{organization}}/{{repository}}.git mqt-{{repository}}
    ```

    :::
    ::::

2.  Change into the project directory:

    ```console
    $ cd mqt-{{repository}}
    ```

3.  Create a branch for local development:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

4.  Install the project and its development dependencies:

    We highly recommend using modern, fast tooling for the development workflow.
    We recommend using [{code}`uv`][uv].
    If you don't have {code}`uv`, follow the installation instructions in the recommendation above (see {ref}`tip above <uv-recommendation>`).
    See the [uv documentation][uv] for more information.

    ::::{tab-set}
    :sync-group: installer

    :::{tab-item} {code}`uv` _(recommended)_
    :sync: uv
    Install the project (including development dependencies) with [{code}`uv`][uv]:

    ```console
    $ uv sync
    ```

    :::
    :::{tab-item} {code}`pip`
    :sync: pip
    If you really don't want to use [{code}`uv`][uv], you can install the project and the development dependencies into a virtual environment using {code}`pip`.

    ```console
    $ python -m venv .venv
    $ source ./.venv/bin/activate
    (.venv) $ python -m pip install -U pip
    (.venv) $ python -m pip install -e . --group dev
    ```

    :::
    ::::

5.  Install pre-commit hooks to ensure code quality:

    The project uses [pre-commit] hooks for running linters and formatting tools on each commit.
    These checks can be run manually via [{code}`nox`][nox], by running:

    ```console
    $ nox -s lint
    ```

    They can also be run automatically on every commit via [{code}`prek`][prek] (recommended).
    To set this up, install {code}`prek`, e.g., via:

    ::::{tab-set}
    :::{tab-item} macOS and Linux

    ```console
    $ curl --proto '=https' --tlsv1.2 -LsSf https://github.com/j178/prek/releases/latest/download/prek-installer.sh | sh
    ```

    :::
    :::{tab-item} Windows

    ```console
    $ powershell -ExecutionPolicy ByPass -c "irm https://github.com/j178/prek/releases/latest/download/prek-installer.ps1 | iex"
    ```

    :::

    :::{tab-item} {code}`uv`

    ```console
    $ uv tool install prek
    ```

    :::
    ::::

    Then run:

    ```console
    $ prek install
    ```

<!-- Links -->

[FetchContent]: https://cmake.org/cmake/help/latest/module/FetchContent.html
[git-submodule]: https://git-scm.com/docs/git-submodule
[nox]: https://nox.thea.codes/en/stable/
[pipx]: https://pypa.github.io/pipx/
[pre-commit]: https://pre-commit.com/
[prek]: https://prek.j178.dev
[ruff]: https://docs.astral.sh/ruff/
[uv]: https://docs.astral.sh/uv/
