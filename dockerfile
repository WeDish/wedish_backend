# syntax=docker/dockerfile:1
FROM python:slim-buster
WORKDIR /app
COPY ./wedish .
COPY ./requirements.txt .
RUN apt update
RUN apt install -y libgtk-3-dev
RUN pip install -r requirements.txt
# RUN python manage.py collectstatic --noinput
# RUN python manage.py migrate
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "wedish.wsgi"]
