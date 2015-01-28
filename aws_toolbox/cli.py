#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import auth
from core import routing

import pprint

def init():
    print 'Retrieving credentials...'
    try:
        auth.init()
    except auth.NoCredentialsFound:
        print 'Please check your credential file or environment variable. RTFM :)'
        exit(1)

    print 'Initializing routes...'
    routing.init()


def main():
    print 'Welcome to the AWS-Toolbox!'

    init()

    # Match a URL, returns a dict or None if no match
    result = routing.match_call('/ec2/instances/2/get_status')
    pprint.pprint(result)


main()
