FROM python:3.10-bullseye as no_dev
# Barebones requirements for a production install.

# TODO: Create a non-root user/group, preferrably with the same UID as the user building it.
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY . .
RUN poetry install --only main

CMD [ "poetry", "run", "cli" ]


FROM no_dev as dev
# Developer friendly stuff.

RUN apt-get update \
    && apt-get install -y bash-completion \
    && poetry completions bash > /etc/bash_completion.d/poetry \
    && poetry install