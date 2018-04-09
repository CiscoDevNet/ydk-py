FROM ubuntu:xenial

MAINTAINER http://ydk.io

COPY . /root/ydk-py

RUN echo 'Installing dependencies  and ydk-py'

WORKDIR /root/ydk-py

RUN /bin/bash -c './dependencies_xenial.sh && ./tests.sh'
