# install python 3.9 image
FROM python:3.11-slim-bookworm
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# pinstall poetry using pip
RUN pip install poetry

# copy poetry files
COPY pyproject.toml* poetry.lock* ./

# install library using poetry (if pyproject.toml exists)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# run uvicorn server
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]