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


class WrongFileFormat(Exception):
    def __init__(self, message):
        self.message = message


class Credentials(object):
    """
    This class is used to retrieve and store AWS credentials.
    """

    def __init__(self, credentials_file_path='/etc/aws-toolbox/credentials.cfg'):
        """
        :param credentials_file_path: The path to the file with AWS credentials
        """
        self.current_region = None
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
        except NoCredentialsFound:
            self._retrieve_by_env()

    def _retrieve_by_file(self):
        """
        Retrieves AWS Credentials from a .cfg file.
        If the file is not found or cannot be read, this method raises a NoCredentialsFound exception.
        """
        if os.path.isfile(self.credentials_file_path) is None:
            raise NoCredentialsFound('No credential file found at %s' % (self.credentials_file_path))

        config = ConfigParser.ConfigParser()
        config.read(self.credentials_file_path)

        try:
            self.current_region = config.get('default', 'region', None)
            self.current_access_key = config.get('default', 'aws_access_key_id', None)
            self.current_secret_access_key = config.get('default', 'aws_secret_access_key', None)
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError) as exception:
            raise WrongFileFormat(exception)

        if self.current_region is None\
                or self.current_access_key is None\
                or self.current_secret_access_key is None:
            raise NoCredentialsFound('Unable to parse the credential file!')

    def _retrieve_by_env(self):
        """
        Retrieves AWS Credentials from a the environment variables
        If the variables does not exist or are empty, this method raises a NoCredentialsFound exception.
        """
        self.current_region = os.environ.get('AWS_ACCESS_KEY_ID', None)
        self.current_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
        self.current_secret_access_key = os.environ.get('AWS_DEFAULT_REGION', None)

        if self.current_region is None\
                or self.current_access_key is None\
                or self.current_secret_access_key is None:
            raise NoCredentialsFound('No credentials found within the environment variables!')
