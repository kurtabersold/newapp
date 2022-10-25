import pytest
from typer.testing import CliRunner

from newapp import cli, __version__

# https://typer.tiangolo.com/tutorial/testing/

runner = CliRunner()


def test_cli_noop():
    result = runner.invoke(cli.app, ["noop"])
    assert result.exit_code == 0


@pytest.mark.skip
def test_cli_null(term_handler):
    # TODO: How to test signal handling in python?
    result = runner.invoke(cli.app, ["null"])
    assert result.exit_code == 0


def test_cli_version():
    result = runner.invoke(cli.app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout
