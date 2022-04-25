# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app
COPY ./src /app
COPY ./requirements.txt /app

RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py
ENV PYTHONPATH "${PYTHONPATH}:${pwd}"
ENV FLASK_RUN_HOST=0.0.0.0
ENV AWS_REGION=""
ENV DB_SECRET=""


EXPOSE 5000

ENTRYPOINT flask run

