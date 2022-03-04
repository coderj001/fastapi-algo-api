FROM python:3.9-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

USER appuser

RUN apk add build-base
RUN apk add g++

ADD . /app/

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN python make.py

CMD [ "python", "main.py" ]
