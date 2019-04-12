FROM ubuntu:xenial

MAINTAINER http://ydk.io

COPY . /root/ydk-py

RUN echo 'Installing dependencies  and ydk-py'

WORKDIR /root/ydk-py

RUN /bin/bash -c './dependencies_xenial.sh && ./dependencies_gnmi.sh && ./tests.sh'

RUN pip3 install ./core/dist/ydk-0.8.2.tar.gz
RUN python3 -c "import ydk.providers"

RUN pip3 install ./gnmi/dist/ydk-service-gnmi-0.4.0.post1.tar.gz
RUN python3 -c "import ydk.gnmi.providers"
