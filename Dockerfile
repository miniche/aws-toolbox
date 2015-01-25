FROM debian:wheezy

MAINTAINER Charles-Emmanuel CAMUS

RUN apt-get -qq update \
    && apt-get -qqy upgrade \
    && apt-get -qqy install --no-install-recommends \
        python \
        python-pip \
    && apt-get clean
