# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app
COPY ./src /app

RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py
ENV PYTHONPATH "${PYTHONPATH}:${pwd}"

EXPOSE 5000

CMD python -m flask --host=0.0.0.0

