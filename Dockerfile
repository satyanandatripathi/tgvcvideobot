FROM python:3.9.7-slim-buster

RUN apt-get update && apt-get upgrade -y 
RUN apt-get install npm -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm@7.22.0
RUN npm i -g npm

COPY . /py
WORKDIR /py
RUN chmod 777 /py

RUN pip3 install --U pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD python3 -m 
