FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update -y
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config -y
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/
