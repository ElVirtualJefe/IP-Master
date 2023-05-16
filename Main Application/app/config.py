# -*- encoding: utf-8 -*-
'''
Copyright (c) 2021 - ElVirtualJefe
'''

import logging
app_logger = logging.getLogger(f'ip-master.{__name__}')
app_logger.debug(f'Entering module {__name__}')

from app.implementations import whoami
from inspect import currentframe

from pathlib import Path
from configparser import ConfigParser

config = ConfigParser()

def _getInitialConfig(configFile=f'{Path(__file__).parent.resolve()}/config.ini',section=None):

    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
    

    app_logger.info(f'Loading config from {configFile}')
    config.read(configFile)

    app_logger.debug(f'Config loaded...')

    return config


def _getDbConfig():
    pass

