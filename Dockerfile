FROM python:3.10-slim

LABEL authors="toxidxd"

RUN apt-get -y update
RUN apt-get -y upgrade

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY . /app/

WORKDIR /app

ENTRYPOINT ["python3", "main.py"]