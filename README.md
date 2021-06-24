# Categories API

### Description
A simple Categories API that stores category tree to database and returns category parents, children and siblings by category id.

**Use of any other third-party libraries or Django extensions (mptt, treebread, etc) is prohibited.**

#### TODO
1. Add unit tests for views
2. Add integration tests (E2E, repositories)

#### Requirements

* [Docker](https://www.docker.com/) >= 18.06.0
* [Docker Compose](https://docs.docker.com/compose/install/) >= 1.23.0


#### Contribution Guide

You can find contribution guide [here](https://kb.epam.com/display/EPMDEPS/Contribution+Guide).

Also you can read a very nice [guide about commit messages](https://m.habr.com/ru/post/416887/).

### How to run project in docker

```bash
make build

make up-d

make logs

make migrate
```

You can find more information about supportable command in the `Makefile`.


### How to work with project

1. Lock poetry dependencies:
    - Activate virtual env
    - Change `pyproject.toml` file
    - Generate `poetry.lock` file: ```poetry lock --no-update```

2. Run tests: `make tests`

3. To create migrations use `make makemigrations` command

4. To run migrations use `make migrate` command

5. To enter inside containers use:
    - `make shell-app`
    - `make shell-db`

6. Linters:
    - `make lint` - run all linters checks:
        - `make format-check` - to check code formatting (black and isort)
        - `make flake8` - to check code formatting (flake8)
        - `make mypy-check` - to check code types using mypy
    - `make format` - to format code using black and isort
    
7. To check project source code metrics you can use [Radon](https://pypi.org/project/radon/): `make radon-check`


## Environment variables

| name | type | required | default |
|------|------|----------|---------|
| POSTGRES_ALCHEMY_DRIVER | str | true | none |
| POSTGRES_HOST | str | true | none |
| POSTGRES_PORT | int | true | none |
| POSTGRES_WORK_DB | str | true | none |
| POSTGRES_WORK_USER | str | true | none |
| POSTGRES_WORK_USER_PASSWORD | str | true | none |
| SECRET_KEY | str | true | none |
| DJANGO_SUPERUSER_USERNAME | str | false | none |
| DJANGO_SUPERUSER_EMAIL | str | false | none |
| DJANGO_SUPERUSER_PASSWORD | str | false | none |


## Notes

It is possible to avoid RecursiveField and create your own realization:
```python
from rest_framework import serializers


class RecursiveField(serializers.Serializer):
    pass


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    children = serializers.ListField(
        child=RecursiveField(), allow_null=True, required=False
    )

    def get_fields(self):
        fields = super().get_fields() or []
        fields['children'] = CategorySerializer(many=True)
        return fields
```
