# Python template repository

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![pre-commit](https://github.com/br3ndonland/template-python/workflows/pre-commit/badge.svg)
![test](https://github.com/br3ndonland/template-python/workflows/test/badge.svg)
[![Build Status](https://travis-ci.com/br3ndonland/template-python.svg?branch=master)](https://travis-ci.com/br3ndonland/template-python)

Brendon Smith ([br3ndonland](https://github.com/br3ndonland/))

## Description

**Welcome!** This is a template repository for Python projects, engineered for use as a [GitHub template repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template). To use the template, click on "Use this template" or browse to [template-python/generate](https://github.com/br3ndonland/template-python/generate). GitHub will create a new repository without the commit history from this one.

Another common approach, especially for Python, is to use [cookiecutter](https://github.com/cookiecutter/cookiecutter). In a cookiecutter repo, the developer adds template variables throughout, like `{{cookiecutter.repo_name}}`. When a user runs `cookiecutter` using the template repository, the template variables are replaced with the information the user provides.

This repo is simple enough that I haven't needed to add cookiecutter yet. The `template-python` repo name can be replaced with a one-line terminal command: `git grep -l 'template-python' | xargs sed -i '' 's/template-python/repo-name/g'` (replace `repo-name` with the name of the repository you generate). There may also be a few edits to the _pyproject.toml_ needed. See the [quickstart](#quickstart) section for more.

## Repository contents

- [.github/](.github): configuration files for [GitHub](https://github.com/).
  - [ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE)
    - [bug_report.md](.github/ISSUE_TEMPLATE/bug_report.md): template for filing a bug report issue on GitHub.
    - [feature_request.md](.github/ISSUE_TEMPLATE/feature_request.md): template for filing a feature request issue on GitHub.
  - [workflows/](.github/workflows)
    - [pre-commit.yml](.github/workflows/pre-commit.yml): [GitHub Actions](https://github.com/features/actions) workflow that runs the pre-commit hooks specified in [.pre-commit-config.yaml](.pre-commit-config.yaml).
    - [test.yml](.github/workflows/test.yml): [GitHub Actions](https://github.com/features/actions) workflow that runs Python tests.
  - [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md): guidelines for behavior when contributing to open-source projects.
  - [CONTRIBUTING.md](.github/CONTRIBUTING.md): detailed instructions for using this repository.
- [.vscode/settings.json](.vscode/settings.json): default settings for [VSCode](https://code.visualstudio.com/).
- [examples/](examples): code samples that can be used to try out the Python tooling in this repo. For more examples, see [my algorithms repo](https://github.com/br3ndonland/algorithms).
- [.pre-commit-config.yaml](.pre-commit-config.yaml): configuration file for [pre-commit](https://pre-commit.com/) specifying [Git pre-commit hooks](https://www.git-scm.com/docs/githooks).
- [.prettierrc](.prettierrc): configuration file for [Prettier](https://prettier.io/docs/en/configuration.html).
- [.travis.yml](.travis.yml): configuration file for [Travis CI](https://docs.travis-ci.com/).
- [LICENSE](LICENSE): [license](https://choosealicense.com/) file describing how the repository may be legally used.
- [poetry.lock](poetry.lock): lock file used by [Poetry](https://python-poetry.org/) to install specific versions of each dependency.
- [pyproject.toml](pyproject.toml): configuration file for [Poetry](https://python-poetry.org/).
- [README.md](README.md): this file, a concise description of the repository

## Quickstart

```sh
❯ cd path/to/repo
# Replace instances of template-python with new repo name
# In the command below, use your repo name instead of 'repo-name'
❯ git grep -l 'template-python' | xargs sed -i '' 's/template-python/repo-name/g'
# Install virtual environment with poetry: https://python-poetry.org/docs/
❯ poetry install
❯ poetry shell
# Install pre-commit hooks
template-python-hash-py3.7 ❯ pre-commit install
# Try running the tests
template-python-hash-py3.7 ❯ pytest
```

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
