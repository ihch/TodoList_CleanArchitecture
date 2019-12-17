FROM python:3.7.5-alpine

MAINTAINER Chihiro Iha <nemu0sou@gmail.com>

RUN mkdir /api

COPY requirements.txt /api

RUN apk add build-base \
  && pip install -r /api/requirements.txt

COPY . /api

WORKDIR /api
CMD python main.py
