# Python template repository

Brendon Smith ([br3ndonland](https://github.com/br3ndonland/))

## Description

**Welcome!** This is a template repository for Python projects, engineered for use as a [GitHub template repository](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/).

## Repository contents

- [.github/](.github) - configuration files for [GitHub](https://github.com/).
  - [ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE)
    - [bug_report.md](.github/ISSUE_TEMPLATE/bug_report.md) - template for filing a bug report issue on GitHub.
    - [feature_request.md](.github/ISSUE_TEMPLATE/feature_request.md) - template for filing a feature request issue on GitHub.
  - [CONTRIBUTING.md](.github/CONTRIBUTING.md) - detailed instructions for using this repository.
- [.vscode/settings.json](.vscode/settings.json) - default settings for [VSCode](https://code.visualstudio.com/).
- [examples/](examples) - code samples that can be used to try out the Python tooling in this repo.
- [.pre-commit-config.yaml](.pre-commit-config.yaml) - configuration file for [pre-commit](https://pre-commit.com/) specifying [Git pre-commit hooks](https://www.git-scm.com/docs/githooks).
- [Dockerfile](Dockerfile) - example [Dockerfile](https://docs.docker.com/engine/reference/builder/) for running Pipenv in Docker.
- [LICENSE](LICENSE) - [license](https://choosealicense.com/) file describing how the repository may be legally used.
- [Pipfile](Pipfile) - [Pipenv](https://pipenv.readthedocs.io/) package list
- [README.md](README.md) - this file, a concise description of the repository

## Quickstart

```sh
❯ cd path/to/repo
❯ pipenv install --dev
❯ pipenv shell
template-python-hash ❯ pre-commit install
```

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
