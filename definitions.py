""" Application definitions that are used throughout the system """
import os
import pathlib
APP_DIR = pathlib.Path(__file__).parent.absolute()


# TODO find better way to handle conditions/env variables
def get_current_env():
    """
    Returns the string of the current environment
    :return: String of current environment
    """
    if os.environ.get('ENVIRONMENT'):
        environment = os.environ.get('ENVIRONMENT')
    elif os.environ.get('DEVENV'):
        environment = os.environ.get('DEVENV')
    else:
        environment = 'LOCAL'
    return environment

