FROM python:3.12-slim
LABEL authors="siiken"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install poetry

COPY ./pyproject.toml ./poetry.lock /app/
COPY ./deployment/dev/scripts/ /scripts
COPY ./src /app/

RUN poetry config virtualenvs.create false \
    && poetry install --with dev \
    && sed -i 's/\r$//' /scripts/run.sh \
    && chmod -R +x /scripts

ENV PATH="/scripts::$PATH"

CMD ["run.sh"]
