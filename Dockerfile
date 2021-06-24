FROM python:3.8.8-slim

ARG APP_USER=category_app
ARG APP_GROUP=category_app
ARG INSTALL_DEV_DEPENDENCIES=false

RUN groupadd $APP_GROUP && useradd -m -s /bin/false -g $APP_GROUP $APP_USER

ENV APP_HOME=/home/$APP_USER/app
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libc6-dev \
    netcat \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache poetry

COPY src/pyproject.toml src/poetry.lock* ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root \
    $(test $INSTALL_DEV_DEPENDENCIES = "false" && echo "--no-dev")

COPY src .

COPY ./scripts/wait-for-it.sh ./scripts/entrypoints/category_app.sh ./

RUN chown -R $APP_USER:$APP_GROUP $APP_HOME

USER $APP_USER

ENTRYPOINT ["./category_app.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8014"]
