# Initial setup
FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt upgrade -y

RUN apt install python3-pip -y
RUN pip install -U pip
RUN pip install scikit-learn numpy pandas

WORKDIR /home

COPY train.csv .
COPY fit.py .
COPY predict.py .

RUN python3 fit.py
copy run.sh .
