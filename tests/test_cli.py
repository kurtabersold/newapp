import signal
import sys

from typer.testing import CliRunner
from unittest import mock

from newapp import cli, __version__

# https://typer.tiangolo.com/tutorial/testing/

runner = CliRunner()


@mock.patch("newapp.cli.sys.exit")
def test_signal_handler(exit_mock):
    cli.signal_handler(signal.SIG_IGN, "I'm a frame!")
    exit_mock.assert_called_once_with(0)


def test_cli_noop():
    result = runner.invoke(cli.app, ["noop"])
    assert result.exit_code == 0


def test_cli_null():
    result = runner.invoke(cli.app, ["null", "--timeout", sys.float_info.min])
    assert result.exit_code == 0


def test_cli_version():
    result = runner.invoke(cli.app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout
