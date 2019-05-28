FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /copycat

WORKDIR /copycat
COPY requirements.txt /copycat/
RUN pip install -r requirements.txt

COPY . /copycat/