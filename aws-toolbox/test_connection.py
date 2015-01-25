# -*- coding: utf-8 -*-

import boto.ec2
import core.auth as awsCore

import pprint

auth = awsCore.Credentials()
auth.retrieve_credentials()

my_ec2 = boto.ec2.connect_to_region(auth.current_location, aws_access_key_id=auth.current_access_key, aws_secret_access_key=auth.current_secret_access_key)
status = my_ec2.get_only_instances('i-9cfa3c5d')

pprint.pprint(status[0].state)
