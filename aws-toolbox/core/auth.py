# -*- coding: utf-8 -*-

"""
    aws-toolbox

    License: MIT
    Created by Charles-Emmanuel (https://github.com/miniche)
"""

import ConfigParser
import os


class NoCredentialsFound(Exception):
    def __init__(self, message):
        self.message = message


class Credentials(object):
    """
    This class is used to retrieve and store AWS credentials.
    """

    def __init__(self, credentials_file_path='/tmp/credentials.cfg'):
        """
        :param credentials_file_path: The path to the file with AWS credentials
        """
        self.current_location = None
        self.current_access_key = None
        self.current_secret_access_key = None
        self.credentials_file_path = credentials_file_path

    def retrieve_credentials(self):
        """
        Tries to retrieve the AWS credentials from the file or from the environment variables.
        :return:
        """
        try:
            self._retrieve_by_file()
        except Exception:
            raise Exception

    def _retrieve_by_file(self):
        """
        Retrieves AWS Credentials from a .cfg file.
        If the file is not found or cannot be read, this method raises a NoCredentialsFound exception.
        """
        if os.path.isfile(self.credentials_file_path) is None:
            raise NoCredentialsFound('No credential file found at %s' % (self.credentials_file_path))

        config = ConfigParser.ConfigParser()
        config.read(self.credentials_file_path)

        self.current_location = config.get('Credentials', 'location', None)
        self.current_access_key = config.get('Credentials', 'access_key', None)
        self.current_secret_access_key = config.get('Credentials', 'secret_access_key', None)

        if self.current_location is None\
                or self.current_access_key is None\
                or self.current_secret_access_key is None:
            raise NoCredentialsFound('Unable to parse the credential file!')
