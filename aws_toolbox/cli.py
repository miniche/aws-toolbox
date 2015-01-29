#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import logging
import sys


def init():

    log.init()

    logging.info('Retrieving credentials...')
    try:
        auth.init()
    except auth.NoCredentialsFound:
        print 'Please check your credential file or environment variable. RTFM :)'
        exit(1)

    logging.info('Initializing routes...')
    routing.init()


def check_arguments():
    if len(sys.argv) != 2:
        print 'Usage: %s action_to_perform' % (sys.argv[0])
        exit(1)

if __name__ == '__main__':
    print 'Welcome to the AWS-Toolbox!'

    # This script is called within the CLI, we add the current file into the sys.path to allow global import
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(path)))

    from aws_toolbox.core import auth
    from aws_toolbox.core import log
    from aws_toolbox.core import routing

    init()
    check_arguments()

    # Match a URL, returns a dict or None if no match
    result = routing.match_call(sys.argv[1])
