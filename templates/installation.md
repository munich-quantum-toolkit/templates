<!--- This file has been generated from an external template. Please do not modify it directly. -->
<!--- Changes should be contributed to https://github.com/munich-quantum-toolkit/templates. -->

# Installation

{%- if project_type == "c++-python" %}
MQT {{name}} is mainly developed as a C++20 library with Python bindings.
The resulting Python package is available on [PyPI](https://pypi.org/project/mqt.{{repository}}/) and can be installed on all major operating systems using all modern Python versions.
{%- elif project_type == "pure-python" %}
MQT {{name}} is developed as a Python package that is available on [PyPI](https://pypi.org/project/mqt.{{repository}}/).
It can be installed on all major operating systems using all modern Python versions.
{%- endif %}

:::::{tip}

We highly recommend using [{code}`uv`][uv].
It is an extremely fast Python package and project manager written in Rust and developed by [Astral](https://astral.sh/) (the same team behind [{code}`ruff`][ruff]).
It can act as a drop-in replacement for {code}`pip` and {code}`virtualenv`, and it provides a more modern and faster alternative to the traditional Python package management tools.
It automatically handles the creation of virtual environments and the installation of packages, and it is much faster than {code}`pip`.
Additionally, it can even set up a Python interpreter for you if it is not installed yet.

If you do not have {code}`uv` installed yet, you can install it via:

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

Check out their excellent [documentation][uv] for more information.

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
In most practical cases (under 64-bit Linux, macOS incl. Apple Silicon, and Windows), this requires no compilation and merely downloads and installs a platform-specific pre-built wheel.
{%- endif %}

Once installed, you can check if the installation was successful:

```console
(.venv) $ python -c "import mqt.{{repository}}; print(mqt.{{repository}}.__version__)"
```

This should print the installed version of the package.

{%- if project_type == "c++-python" %}

## Building From Source for Performance

In order to get the best performance and enable platform-specific optimizations that cannot be enabled on portable wheels, it is recommended to build the library from source:

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

This requires a [C++ compiler supporting C++20](https://en.wikipedia.org/wiki/List_of_compilers#C++_compilers) and a minimum [CMake](https://cmake.org/) version of 3.24.

{%- endif %}

## Integrating MQT {{name}} Into Your Project

If you want to use the MQT {{name}} Python package in your own project, you can simply add it as a dependency in your {code}`pyproject.toml` or {code}`setup.py` file.
This will automatically install the MQT {{name}} package when your project is installed.

::::{tab-set}

:::{tab-item} {code}`uv` _(recommended)_

```console
$ uv add mqt.core
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

:::{tab-item} {code}`setup.toml`

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

This is the recommended approach for projects because it allows to detect installed versions of MQT Core and only downloads the library if it is not available on the system.
Furthermore, CMake's [{code}`FetchContent`][FetchContent] module allows for lots of flexibility in how the library is integrated into the project.

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
  GIT_REPOSITORY https://github.com/${MQT_CORE_REPO_OWNER}/{{repository}}.git
  GIT_TAG ${MQT_{{name.upper()}}_REV}
  FIND_PACKAGE_ARGS ${MQT_{{name.upper()}}_MINIMUM_VERSION})
list(APPEND FETCH_PACKAGES mqt-{{repository}})

# Make all declared dependencies available.
FetchContent_MakeAvailable(${FETCH_PACKAGES})
```

:::

:::{tab-item} {code}`git-submodule`

Integrating the library as a [{code}`git` submodule][git-submodule] is the simplest approach.
However, handling {code}`git` submodules can be cumbersome, especially when working with multiple branches or versions of the library.
First, add the submodule to your project (e.g., in the {code}`external` directory):

```console
$ git submodule add https://github.com/{{organization}}/{{repository}}.git external/mqt-{{repository}}
```

Then, add the following line to your {code}`CMakeLists.txt` to make the library's targets available in your project:

```cmake
add_subdirectory(external/mqt-{{repository}})
```

:::

:::{tab-item} {code}`find_package()`

MQT {{name}} can be installed on your system after building it from source:

```console
$ git clone https://github.com/{{organization}}/{{repository}}.git mqt-{{repository}}
$ cd mqt-{{repository}}
$ cmake -S . -B build
$ cmake --build build
$ cmake --install build
```

Then, in your project's {code}`CMakeLists.txt`, you can use the {code}`find_package()` command to locate the installed library:

```cmake
find_package(mqt-{{core}} <version> REQUIRED)
```

::::

{%- endif %}

(development-setup=)

## Development Setup

You want to contribute to MQT {{name}}?
Below, you can find instructions on how to setup your development environment.
Refer to {doc}`contributing` for a detailed contribution guide.

1.  Get the code:

    ::::{tab-set}
    :::{tab-item} External Contribution
    If you do not have write access to the [{{organization}}/{{repository}}](https://github.com/{{organization}}/{{repository}}) repository, fork the repository on GitHub (see <https://docs.github.com/en/get-started/quickstart/fork-a-repo>) and clone your fork locally.

    ```console
    $ git clone git@github.com:your_name_here/{{repository}}.git
    ```

    :::
    :::{tab-item} Internal Contribution
    If you do have write access to the [{{organization}}/{{repository}}](https://github.com/{{organization}}/{{repository}}) repository, clone the repository locally.

    ```console
    $ git clone git@github.com/{{organization}}/{{repository}}.git
    ```

    :::
    ::::

2.  Change into the project directory:

    ```console
    $ cd {{repository}}
    ```

3.  Create a branch for local development:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

4.  Install development tools:

    We highly recommend using modern and fast tooling for the development workflow.
    {%- if project_type == "c++-python" %}
    If you plan to [work on the Python package](#working-on-the-python-package), we highly recommend using [{code}`uv`][uv].
    {%- elif project_type == "pure-python" %}
    We highly recommend using [{code}`uv`][uv].
    {%- endif %}
    It is an extremely fast Python package and project manager written in Rust and developed by [Astral](https://astral.sh/) (the same team behind [{code}`ruff`][ruff]).
    It can act as a drop-in replacement for {code}`pip` and {code}`virtualenv`, and it provides a more modern and faster alternative to the traditional Python package management tools.
    It automatically handles the creation of virtual environments and the installation of packages, and it is much faster than {code}`pip`.
    Additionally, it can even set up a Python interpreter for you if it is not installed yet.

    If you do not have {code}`uv` installed yet, you can install it via:

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

    Check out their excellent [documentation][uv] for more information.

    We also highly recommend installing and setting up [{code}`pre-commit`][pre-commit] to automatically run a set of checks before each commit, and [{code}`nox`][nox] for automating common development tasks.

    ::::{tab-set}
    :::{tab-item} {code}`uv` _(recommended)_
    :sync: uv
    The easiest way to install {code}`pre-commit` and {code}`nox` is via [{code}`uv`][uv].

    ```console
    $ uv tool install pre-commit
    $ uv tool install nox
    ```

    :::
    :::{tab-item} {code}`brew`
    :sync: brew
    If you use macOS and Homebrew, you can install {code}`pre-commit` and {code}`nox` with:

    ```console
    $ brew install pre-commit nox
    ```

    :::
    :::{tab-item} {code}`pipx`
    :sync: pipx
    If you prefer to use [{code}`pipx`][pipx], you can install {code}`pre-commit` and {code}`nox` with:

    ```console
    $ pipx install pre-commit
    $ pipx install nox
    ```

    :::
    :::{tab-item} {code}`pip`
    :sync: pip
    If you prefer to use regular {code}`pip` (preferably in a virtual environment), you can install {code}`pre-commit` and {code}`nox` with:

    ```console
    $ pip install pre-commit nox
    ```

    :::
    ::::

    Afterward, you can set up the {code}`pre-commit` hooks with:

    ```console
    $ pre-commit install
    ```

<!-- Links -->

[FetchContent]: https://cmake.org/cmake/help/latest/module/FetchContent.html
[git-submodule]: https://git-scm.com/docs/git-submodule
[ruff]: https://docs.astral.sh/ruff/
[uv]: https://docs.astral.sh/uv/
