import logging
import signal
import sys

import typer

from . import __version__ as app_version

# TODO: Install completion in dev environment.

log = logging.getLogger(__name__)
app = typer.Typer()


def signal_handler(signum, frame):
    log.info(
        {
            "message": "Handling Signal",
            "signal": signal.Signals(signum).name,
            "sig_num": signum,
            "frame": frame,
        }
    )
    sys.exit(0)


@app.command()
def noop():
    """No-Op Command"""
    log.info("noop")
    return True


@app.command()
def null(timeout=0):
    """Do Nothing Forever"""
    from threading import Event

    log.info("Waiting forever")

    signal.signal(signal.SIGTERM, signal_handler)
    Event().wait()


@app.command()
def version():
    """App Version"""
    typer.echo(app_version)


if __name__ == "__main__":
    app()
