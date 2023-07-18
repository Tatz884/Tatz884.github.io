# install python 3.9 image
FROM python:3.11-slim-bookworm
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install --no-cache-dir -r requirements.txt

# run uvicorn server
ENTRYPOINT ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]