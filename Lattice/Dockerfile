FROM debian:stable-slim
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources


RUN apt-get update
RUN apt-get install -y socat 
RUN apt-get install -y sagemath

RUN apt install -y python3-pip

RUN pip install pycryptodome --break-system-packages

RUN mkdir /app

WORKDIR /app
COPY challenge.py .

CMD ["/bin/sh", "-c", "socat TCP-LISTEN:23333,fork,reuseaddr EXEC:'python3 challenge.py',stderr"]
