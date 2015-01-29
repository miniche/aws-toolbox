#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys


def init():
    print 'Retrieving credentials...'
    try:
        auth.init()
    except auth.NoCredentialsFound:
        print 'Please check your credential file or environment variable. RTFM :)'
        exit(1)

    print 'Initializing routes...'
    routing.init()


if __name__ == '__main__':
    print 'Welcome to the AWS-Toolbox!'

    # This script is called within the CLI, we add the current file into the sys.path to allow global import
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(path)))

    from aws_toolbox.core import auth
    from aws_toolbox.core import routing

    init()

    # Match a URL, returns a dict or None if no match
    result = routing.match_call('/ec2/instances/2/get_status')
