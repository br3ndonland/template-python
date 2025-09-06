# template-python

[![ci](https://github.com/br3ndonland/template-python/workflows/ci/badge.svg)](https://github.com/br3ndonland/template-python/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Description

**Welcome!** This is a template repository for Python projects, engineered for use as a [GitHub template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template). To use the template, click on "[Use this template](https://github.com/new?template_name=template-python&template_owner=br3ndonland)" or use the [GitHub CLI](https://cli.github.com/manual/) (` gh repo create your-repo-name --public --template br3ndonland/template-python`).

The template repo name can be replaced as shown in the [quickstart](#quickstart) section.

## Quickstart

[Install Hatch](https://hatch.pypa.io/latest/install/), rename the project, then install the project:

```sh
❯ cd path/to/repo
# Replace instances of template-python with new repo name
# In the command below, use your repo name instead of 'repo-name'
❯ git grep -l 'template-python' | xargs sed -i '' 's|template-python|repo-name|g'
❯ git grep -l 'template_python' | xargs sed -i '' 's|template_python|repo-name|g'
# Try running the tests
❯ hatch run coverage run
```

## Documentation

Documentation is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

The [Vercel project configuration](https://vercel.com/docs/project-configuration) in [`vercel.json`](vercel.json) can be used to deploy the docs to [Vercel](https://vercel.com/docs).

## Contributing

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Related

Another common approach, especially for Python, is to use [cookiecutter](https://github.com/cookiecutter/cookiecutter). In a cookiecutter repo, the developer adds template variables throughout, like `{{cookiecutter.repo_name}}`. When a user runs `cookiecutter` using the template repository, the template variables are replaced with the information the user provides. This repo is simple enough that I haven't needed to add cookiecutter yet.

[Copier](https://copier.readthedocs.io/en/stable/) and [PyScaffold](https://pyscaffold.org/en/stable/) are similar to cookiecutter, with some additional benefits.
