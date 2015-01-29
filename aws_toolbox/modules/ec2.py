# -*- coding: utf-8 -*-

import pprint

import boto.ec2

from aws_toolbox.core.auth import current_credentials


class EC2(object):
    def __init__(self):
        self.connection = boto.ec2.connect_to_region(
            current_credentials.current_region,
            aws_access_key_id=current_credentials.current_access_key,
            aws_secret_access_key=current_credentials.current_secret_access_key
        )

    def get_status(self, context):
        status = self.connection.get_only_instances(context['id'])

        pprint.pprint(status[0].state)
