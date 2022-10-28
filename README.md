# newapp

This is not a real app, It's just a template.


## Invoke Tasks
This project uses [invoke](https://pypi.org/project/invoke/). It's purpose is to facilitate
execution of tasks from your dev machine to a docker container.

```
$ inv -l
Available tasks:

  build   Build Docker Image
  cli     Run a CLI command
  down    Stop docker-compose stack
  logs    Tail docker-compose logs
  sh      Open a login shell in a running container
  test    Run tests
  up      Start docker-compose stack
```

### Shell Completion
TODO: Document how to add invoke shell completion.


## Typer (`cli.py`)
This project uses [typer](https://pypi.org/project/typer/) It's purpose is to create a common entrypoint interface which can
collect arguments, and run whatever code needed.

```
$ poetry run cli --help
Usage: cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  noop     No-Op Command
  null     Do Nothing Forever
  version  App Version
```

## Poetry
This project uses [poetry](https://pypi.org/project/poetry/) for dependency management.

### Update
`poetry update`

### Add Dependency
`poetry add [--dev] package`




## TODO
* Add more documentation
* Convert to [cookiecutter](https://pypi.org/project/cookiecutter/) template