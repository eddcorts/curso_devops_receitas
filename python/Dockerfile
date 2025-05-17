FROM python:3.13-slim as python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry" \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
RUN apt-get update --fix-missing
RUN apt-get install --no-install-recommends -y \
    libpq-dev -y

# builder-base is used to build dependencies --------------
FROM python-base as builder-base
RUN pip install --upgrade pip \
    && apt-get install --no-install-recommends -y \
    curl build-essential libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN rm -rf "${POETRY_HOME:-~/.poetry}"
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    chmod a+x /opt/poetry/bin/poetry

# Copy our Python requirements to cache them
# and install only runtime deps using poetry
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --without dev --no-root

# ---------------------------------------------------------
FROM python-base

RUN addgroup --system app && adduser --no-create-home --system --group app
USER app

# Copying poetry and venv into image
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Copying in our entrypoint
COPY /docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR $PYSETUP_PATH
RUN poetry install --without dev --no-root

WORKDIR /back
COPY src src
COPY pyproject.toml poetry.lock ./

EXPOSE 8888
ENTRYPOINT /docker-entrypoint.sh $0 $@

# previously, poetry itself was isolated from the final image.
# but now, we use `poe` to run the server to ensure the virtual env, so
# unfortunately in the end we still need poetry installed
CMD ["poe", "start"]
