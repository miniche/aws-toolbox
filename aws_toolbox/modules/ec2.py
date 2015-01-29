# -*- coding: utf-8 -*-

import logging
import time

import pprint

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
        Gets the current status of the given instance.
        :param context: Requires an instance ID
        :return: Dict
        """
        instances_data = self.connection.get_only_instances(context['id'])
        return instances_data[0].state

    def wait_started(self, context):
        """
        Waits until the EC2 instance is up.
        :param context: Requires an instance ID
        """
        for i in range(0, 30):
            status = self.get_status(context)

            if status == 'running':
                logging.info('Instance is now running!')
                return True
            elif status == 'stopped':
                logging.info('This instance is stopped. Tips: run a start instance command before.')
                return False
            else:
                logging.info('Current status: %s. Waiting...' % (status))

            time.sleep(5)

        logging.info('Instance stills unavailable. Exiting.')
        return False
