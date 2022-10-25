FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY . .
RUN poetry install

# TODO: Install typer shell completion?

CMD [ "poetry", "run", "cli" ]
