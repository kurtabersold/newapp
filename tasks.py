import invoke

dev = "develop"


@invoke.task
def build(c):
    """Build Docker Image"""
    c.run("docker-compose build")


@invoke.task
def up(c):
    """Start docker-compose stack"""
    c.run("docker-compose up -d")


@invoke.task
def down(c):
    """Stop docker-compose stack"""
    c.run("docker-compose down")


@invoke.task
def logs(c):
    """Tail docker-compose logs"""
    c.run("docker-compose logs --follow")


@invoke.task(help={
    "service": f"docker-compose service name (Default: {dev}",
})
def test(c, service=dev):
    """Run tests"""
    c.run(f"docker-compose run --rm {service} poetry run pytest", pty=True)


@invoke.task(help={
    "service": f"docker-compose service name (Default: {dev}",
})
def sh(c, service=dev):
    """Open a login shell in a running container"""
    c.run(f"docker-compose exec {service} bash -l", pty=True)


@invoke.task(help={
    "service": f"docker-compose service name (Default: {dev}",
    "arg": "argument string to pass to typer cli app (Default: --help)"
})
def cli(c, service=dev, arg=""):
    """Run a CLI command"""
    c.run(f"docker-compose exec {service} poetry run cli {arg}", pty=True)
