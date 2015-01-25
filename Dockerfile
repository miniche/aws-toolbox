FROM debian:wheezy

MAINTAINER Charles-Emmanuel CAMUS

ENV AWS_ACCESS_KEY null
ENV AWS_SECRET_ACCESS_KEY null

RUN apt-get -qq update \
    && apt-get -qqy upgrade \
    && apt-get -qqy install --no-install-recommends \
        python \
        python-pip \
    && apt-get clean

COPY aws-toolbox /opt/aws-toolbox

RUN pip install -r /opt/aws-toolbox/requirements.txt
