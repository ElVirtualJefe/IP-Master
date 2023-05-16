import logging
app_logger = logging.getLogger(f'ip-master.{__name__}')
app_logger.debug(f'Entering module {__name__}')

from inspect import currentframe


from inspect import getframeinfo

def whoami(frame): 
#    frame = inspect.currentframe()
    return getframeinfo(frame).function


clients = {}

def build_clients():
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    from app.implementations import ipAddress
    from app.config import config
    clients['ipAddress'] = ipAddress.ipAddressClient(config=config['main_app'])
    #client.append(ipAddress.ipAddressClient(config=config['main_app']))
    app_logger.debug(f'{clients}')

    app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')

