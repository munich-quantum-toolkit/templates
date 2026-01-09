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

4.  Install development dependencies:

    We highly recommend using modern, fast tooling for the development workflow.
    We recommend using [{code}`uv`][uv].
    If you don't have {code}`uv`, follow the installation instructions in the recommendation above (see {ref}`tip above <uv-recommendation>`).
    See the [uv documentation][uv] for more information.

    ::::{tab-set}
    :sync-group: installer

    :::{tab-item} {code}`uv` _(recommended)_
    :sync: uv
    Install the dependencies (including testing and documentation dependencies) with [{code}`uv`][uv] with:

    ```console
    $ uv sync --group dev --group docs
    ```

    :::
    :::{tab-item} {code}`pip`
    :sync: pip
    If you really don't want to use [{code}`uv`][uv], you can export the dependencies into a {code}`requirements.txt` and install into a virtual environment using {code}`pip`

    ```console
    $ uv export --group docs --no-hashes > requirements.txt
    $ python -m venv .venv
    $ source ./.venv/bin/activate
    (.venv) $ python -m pip install -r requirements.txt
    ```

    :::
    ::::

5.  Linting:

    Linting is handled by [{code}`nox`][nox], by running:

    ```console
    $ nox -s lint
    ```

    There are also [{code}`prek`][prek] hooks available, which allow you to automatically run linting every time you commit.

    To set this up, [install {code}`prek`](https://prek.j178.dev/installation/), then run:

    ```console
    $ prek install
    ```

<!-- Links -->

[FetchContent]: https://cmake.org/cmake/help/latest/module/FetchContent.html
[git-submodule]: https://git-scm.com/docs/git-submodule
[nox]: https://nox.thea.codes/en/stable/
[pipx]: https://pypa.github.io/pipx/
[prek]: https://prek.j178.dev
[ruff]: https://docs.astral.sh/ruff/
[uv]: https://docs.astral.sh/uv/
