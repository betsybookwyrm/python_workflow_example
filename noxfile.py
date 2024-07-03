import nox

test_pythons = ["3.11", "3.12"]

# These are the default sessions to run when nox is called with no sessions
# specified i.e. `nox`
nox.options.sessions = ["lint", "test"]
# Other sessions can be run with the -s option
# e.g. `nox -s build_docs`

# Other nox settings
nox.options.stop_on_first_error = True
nox.options.error_on_missing_interpreters = True


@nox.session()
def formatting_recs(session):
    """
    Shows recommended formatting changes (using black)

    Black config can be found in pyproject.toml
    """
    session.install("-r", "requirements-tidy.txt")
    session.run("black", "--diff", ".")


@nox.session()
def format(session):
    """
    Makes all code Black-compliant

    Black config can be found in pyproject.toml
    """
    session.install("-r", "requirements-tidy.txt")
    session.run("black", ".")


@nox.session(python=test_pythons)
def lint(session):
    """Check PEP8 and formatting"""
    # session.install("flake8")
    session.install("-r", "requirements-tidy.txt")
    session.install(".")

    session.run("flake8")

    try:
        # Black config can be found in pyproject.toml
        session.run("black", "--version")
        session.run("black", "--check", ".")
    except nox.command.CommandFailed:
        session.notify("formatting_recs")
        raise


@nox.session(python=test_pythons)
def test(session):
    session.install("-r", "requirements-dev.txt")
    session.install("-r", "requirements-tidy.txt")

    session.run("pytest")


# May also want to have build_docs session if using sphinx,
# and other build and deploy sessions as needed
