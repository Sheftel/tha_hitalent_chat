FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /project
COPY requirements.txt /project/

RUN pip install -r requirements.txt

COPY . /project/