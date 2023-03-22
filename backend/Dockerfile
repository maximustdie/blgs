FROM python:3.10
WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /backend/src

