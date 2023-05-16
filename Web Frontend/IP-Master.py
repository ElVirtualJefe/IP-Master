# -*- encoding: utf-8 -*-
'''
Copyright (c) 2021 - ElVirtualJefe
'''
from pathlib import Path
import logging

FORMATTER = logging.Formatter('%(asctime)s.%(msecs)dZ %(name)s %(processName)s[%(process)d]: %(levelname)s >>> %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')
    

def _setup_extra_logging(config):
    from logging.handlers import RotatingFileHandler,SysLogHandler

    app_logger = logging.getLogger('ip-master')
    app_logger.info(f'Configuring extra logging options...')

    try:
        log_file = config.get('LOG_FILE','ip_master.log')
#    except:
#        log_file = 'ip_master.log'

#    try:
        tmp_dir = config.get('LOG_LOCATION',f'{Path(__file__).parent.resolve()}/logs')
        log_dir = Path(tmp_dir).absolute()
#    except:
#        log_dir = f'{Path(__file__).parent.resolve()}/logs'
    
        app_logger.debug(f'log_file = {log_dir}/{log_file}')
    
#    try:
        match config.get('LOG_LEVEL',None):
            case 'DEBUG':
                log_level = logging.DEBUG
            case 'INFO':
                log_level = logging.INFO
            case 'WARN':
                log_level = logging.WARN
            case 'ERROR':
                log_level = logging.ERROR
            case 'CRITICAL':
                log_level = logging.CRITICAL
            case _:
                log_level = logging.WARN
#    except:
#        log_level = logging.WARN
    
#    try:
        log_file_max_size = int(config.get('LOG_FILE_MAX_SIZE',5120)) * 1024
#    except:
#        log_file_max_size = 5120 * 1024

        fileLogHandler = RotatingFileHandler(f'{log_dir}/{log_file}',maxBytes=log_file_max_size)
        fileLogHandler.setLevel(log_level)
        fileLogHandler.setFormatter(FORMATTER)
        app_logger.addHandler(fileLogHandler)
    
    except:
        app_logger.warn('File Logging error', exc_info=True)

    try:
        if config.get('LOG_REMOTE_SYSLOG',False) == True:
            remote_syslog = config['LOG_REMOTE_SYSLOG_ADDRESS']
            remote_syslog_port = int(config['LOG_REMOTE_SYSLOG_PORT'])

            syslogHandler = SysLogHandler(address=(remote_syslog,remote_syslog_port))
            syslogHandler.setFormatter(FORMATTER)
            syslogHandler.setLevel(log_level)
            app_logger.addHandler(syslogHandler)
        else:
            app_logger.debug('Remote syslog is disabled')
    except:
        app_logger.debug('Not configuring remote syslog because of errors...')

    app_logger.info('Extra logging configuration completed')


def main():
    # Setup initial logging...

    app_logger = logging.getLogger('ip-master')
    app_logger.setLevel(logging.DEBUG)

    conLogHandler = logging.StreamHandler()
    conLogHandler.setLevel(logging.DEBUG)
    conLogHandler.setFormatter(FORMATTER)

    app_logger.addHandler(conLogHandler)

    app_logger.debug(f'Initializing the IP Master appliction...')

    from app.config import _getInitialConfig
    app_logger.debug(f'Get initial configuration file')
    config = _getInitialConfig(f'{Path(__file__).parent.resolve()}/config.ini')

    _setup_extra_logging(config['logging'])


    app_logger.info("Loading IP Master app...")

    try:
        import app
        #app.test(config)
        from app.implementations import build_clients,clients
        app_logger.debug(f'clients = {clients}')
        build_clients()
        app_logger.debug(f'clients = {clients}')
        app.server(config)
    except:
#        app_logger.exception(f'Something is broken...',exc_info=True)
        app_logger.error(f'Something is broken...',exc_info=True)

    app_logger.info("Closing IP Master app...")


if __name__ == '__main__':
    main()
