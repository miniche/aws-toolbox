FROM debian:wheezy

MAINTAINER Charles-Emmanuel CAMUS

ENV AWS_ACCESS_KEY_ID null
ENV AWS_SECRET_ACCESS_KEY null
ENV AWS_DEFAULT_REGION null

RUN apt-get -qq update \
    && apt-get -qqy upgrade \
    && apt-get -qqy install --no-install-recommends \
        python \
        python-pip \
    && apt-get clean

COPY aws_toolbox /opt/aws_toolbox

RUN pip install -r /opt/aws_toolbox/requirements.txt
RUN pip install awscli

VOLUME /etc/aws-toolbox/
