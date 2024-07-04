# Python Workflow example

This repository is meant as an experimental and demonstration space for some elements of my Python development workflow. This is all highly opinionated and probably not optimal - it's just the result of building up habits and occasionally changing tooling over time.

I'm not releasing it as open source right now for the above reason. Current license for the whole thing is CC-BY 4.0, though if you're just pulling pieces from the code and config you are welcome to do so freely and without attribution.


## Python environment management
### Python installations

I use [pyenv](https://github.com/pyenv/pyenv) and pyenv-virtualenv (install both with [pyenv-installer](https://github.com/pyenv/pyenv-installer)). Hence all repositories have a `.python-version` file locally. I don't commit that file to shared repositories so as to not add uncessary files for those who use different environment management tooling.



### Python packaging
- In the past I've generally preferred to omit a `src` folder if there is only one base module in the repository, but I think the `src` system is winning me over now.
- `pyproject.toml` for packaging. `setuptools` for build.

Resources:
- [PyPA's Sample Project](https://github.com/pypa/sampleproject)
- [Python Packaging User Guide](https://packaging.python.org)

Use [semantic versioning](https://semver.org/). Depending on the collaboration workflow, either use a ``__version__`` attribute in the top-level `__init__.py` to declare the version, or use the git tag via [setuptools-scm](https://pypi.org/project/setuptools-scm/).

When it matures, [validate-pyproject](https://validate-pyproject.readthedocs.io) looks like a useful tool.

### Requirements / dependencies

I use pip and `requirements.txt` (sometimes multiple requirements files for different purposes, such as a separate `requirements-dev.txt`).

List unpinned dependencies (with minimum versions where known) in `pyproject.toml`, and then use `pip-compile` (part of [`pip-tools`](https://pypi.org/project/pip-tools/) or `pip freeze` (for informal things with no `pyproject.toml`) to generate pinned requirements.txt files.

Using pip-compile (assuming reqs are in `pyproject.toml`):

1. `pip-compile -o requirements.txt pyproject.toml`
2. `pip-compile --extra dev -o requirements-dev.txt pyproject.toml`

If you want to install pinned versions, pip install from the requirements files before (or after) installing the package. If you don't care, just pip install the package itself.

Note - might want to switch over to .in files instead of listing requirements directly in pyproject.toml - would enable better control e.g. https://github.com/jazzband/pip-tools?tab=readme-ov-file#workflow-for-layered-requirements


## Linting

I always use [flake8](https://flake8.pycqa.org/), and for collaborative projects always use [black](https://black.readthedocs.io). I use the [minimal black compatibility config for flake8](https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html#minimal-configuration)

Note that [black has editor integrations](https://black.readthedocs.io/en/stable/integrations/editors.html).

## Testing

[pytest](https://docs.pytest.org/) with liberal use of fixtures

## Managing tidying and testing tasks
### Nox

I use [nox](https://nox.thea.codes) both to facilitate testing/building across multiple Python versions and to standardise test, lint, deploy, etc config across development environments and CI/CD.

Alternatives:
- tox: very old, still fairly common in the Python world, but I prefer nox's flexibility due to being configured in Python code
- [just](https://just.systems/): haven't used this one but it looks very handy if you want a simple make-style way to save sets of commands that isn't Python-specific

### CI/CD etc
### Pre-commit

[Pre-commit](https://pre-commit.com) is an amazing tool that uses git pre-commit hooks to automatically call whatever checks you want on your staged changes when you make a git commit. I love pre-commit!

Pre-commit hooks are configured in this repository for black and flake8 as well as a few miscellaneous checks for things like trailing whitespace. See `.pre-commit-config.yaml`. Note that if any of the hooks fail their checks of your changes or make changes themselves, you will need to re-stage the changed files and re-run the commit.

Don't forget to run `pre-commit install` on first checkout or on any changes to the precommit config.

My fave pre-commit hook isn't actually in this repository - [nbstripout](https://github.com/kynan/nbstripout) is a lifesaver when using Jupyter Notebooks.

## Git config
## Git workflow
## Python frameworks

Here are some of my faves:

- [Click](https://click.palletsprojects.com) for command-line applications, though argparse is fine for a very simple interface or an informal script

## Environment variables

direnv/dotenv

## Type hinting

Essential for anything meant for use as a library.

### Static type checking

Still playing with tools/systems - maybe [mypy](https://mypy.readthedocs.io) or [pyright](https://github.com/microsoft/pyright)?

Further reading:
- https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md

## Docs

Small scale: handful of markdown files.

Large scale: Sphinx.

Both mermaid.js and draw.io are invaluable for diagrams. If the latter, commit the SVG to git. If the former, the code should be in your markdown file.

## Logging

... add this later
