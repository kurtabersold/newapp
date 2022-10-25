import invoke

dev = "develop"


@invoke.task
def build(c):
    """Build Docker Image"""
    c.run("docker-compose build")


@invoke.task
def up(c):
    """Up"""
    c.run("docker-compose up -d")


@invoke.task
def down(c):
    """Down"""
    c.run("docker-compose down")


@invoke.task
def logs(c):
    """Logs"""
    c.run("docker-compose logs --follow")


@invoke.task
def test(c, container=dev):
    """Test"""
    c.run(f"docker-compose exec {container} poetry run pytest", pty=True)


@invoke.task
def sh(c, container=dev):
    """Shell"""
    c.run(f"docker-compose exec {container} bash -l", pty=True)
