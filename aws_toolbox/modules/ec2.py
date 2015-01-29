# -*- coding: utf-8 -*-

import boto.ec2

from aws_toolbox.core.auth import current_credentials


class EC2(object):
    """
    Manages EC2 instances
    """

    def __init__(self):
        self.connection = boto.ec2.connect_to_region(
            current_credentials.current_region,
            aws_access_key_id=current_credentials.current_access_key,
            aws_secret_access_key=current_credentials.current_secret_access_key
        )

    def get_status(self, context):
        """
        Get the current status of the given instance.
        :param context: Requires an instance ID
        :return: Dict
        """
        return self.connection.get_only_instances(context['id'])[0]
