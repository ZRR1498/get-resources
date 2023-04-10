FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/

RUN pip install --upgrade pip

WORKDIR /backend/backend/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
