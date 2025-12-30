FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update -y
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config -y
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

# Command to run Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_docker_django_app.wsgi:application"]
