FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=true

RUN apk update
RUN apk add build-base
RUN apk add g++

RUN echo "Asia/Kolkata" > /etc/timezone &&  cp /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

COPY requirements.txt /app/requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ADD . /app

WORKDIR /app

RUN python make.py

EXPOSE 8000

CMD [ "python", "main.py" ]
