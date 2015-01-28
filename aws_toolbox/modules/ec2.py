# -*- coding: utf-8 -*-

import pprint

import boto.ec2

from core.auth import current_credentials


def toto():
    print 'toto'


class EC2(object):
    def __init__(self):
        self.connection = boto.ec2.connect_to_region(
            current_credentials.current_region,
            aws_access_key_id=current_credentials.current_access_key,
            aws_secret_access_key=current_credentials.current_secret_access_key
        )

    def get_status(self):
        status = self.connection.get_only_instances('i-9cfa3c5d')

        pprint.pprint(status[0].state)
