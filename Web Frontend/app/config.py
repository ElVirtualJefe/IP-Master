# -*- encoding: utf-8 -*-
'''
Copyright (c) 2021 - ElVirtualJefe
'''

import logging
from app.implementations import whoami
from inspect import currentframe

app_logger = logging.getLogger(f'ip-master.{__name__}')
app_logger.debug(f'Entering module {__name__}')

from pathlib import Path
import logging


def _getInitialConfig(configFile=f'{Path(__file__).parent.resolve()}/config.ini',section=None):
    from configparser import ConfigParser

    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
    

    app_logger.info(f'Loading config from {configFile}')
    config = ConfigParser()
    config.read(configFile)

    app_logger.debug(f'Config loaded...')

    return config


def _getDbConfig():
    pass

