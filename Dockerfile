ARG UID=${UID:-1000}
FROM python:3.10-bullseye as prod
ARG UID
# Barebones requirements for a production install.

ENV PYTHONDONTWRITEBYTECODE=1
ENV APPNAME=newapp

# root stuff
# RUN ???

# app user stuff
RUN groupadd --gid $UID $APPNAME \
    && useradd -ms /bin/bash --uid $UID --gid $UID $APPNAME
USER $APPNAME
ENV PATH="$PATH:/home/$APPNAME/.local/bin"

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir poetry && poetry install --only main
CMD [ "poetry", "run", "cli" ]


FROM prod as dev
# Developer friendly stuff.

# root stuff
USER root
# https://github.com/python-poetry/poetry/issues/4572
#RUN apt-get update \
#    && apt-get install -y bash-completion \
#    && poetry completions bash > /etc/bash_completion.d/poetry

# app user stuff
USER $APPNAME
RUN poetry install