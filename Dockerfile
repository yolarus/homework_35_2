FROM python:3.13

WORKDIR /code

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf var/libv/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

COPY . /code/
