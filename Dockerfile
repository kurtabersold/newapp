ARG UID=${UID:-1000}
FROM python:3.10-bullseye as prod
ARG UID
# Barebones requirements for a production install.

ENV APPNAME=newapp \
    APPDIR="/app" \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/etc/poetry" \
    PATH="$PATH:/etc/poetry/bin"

# root stuff
WORKDIR $APPDIR
COPY . .
RUN groupadd --gid $UID $APPNAME \
    && useradd -ms /bin/bash --uid $UID --gid $UID $APPNAME \
    && chown --recursive $APPNAME:$APPNAME $APPDIR \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version \
    && echo "export PATH=\$PATH:$POETRY_HOME/bin\nsource \$(poetry env info --path)/bin/activate" \
    > /etc/profile.d/activate_poetry.sh \
    && chmod +x /etc/profile.d/activate_poetry.sh

# app user stuff
USER $APPNAME
RUN poetry install --only main
CMD [ "poetry", "run", "cli" ]


FROM prod as dev
# Developer friendly stuff.

# root stuff
# USER root
# TODO: https://github.com/python-poetry/poetry/issues/4572
#RUN DEBIAN_FRONTEND=noninteractive apt-get update \
#    && apt-get install -y --no-install-recommends bash-completion \
#    && poetry completions bash > /etc/bash_completion.d/poetry

# app user stuff
USER $APPNAME
RUN poetry install