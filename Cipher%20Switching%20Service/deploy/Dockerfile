FROM python:slim

RUN apt-get update && apt-get install -yqq socat

RUN pip install gmpy2 pycryptodome
RUN mkdir /app

WORKDIR /app
COPY challenge.py .

CMD ["/bin/sh", "-c", "socat TCP-LISTEN:8763,fork,reuseaddr EXEC:'python challenge.py',stderr"]
