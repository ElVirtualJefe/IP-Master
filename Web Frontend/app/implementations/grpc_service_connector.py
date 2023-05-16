import logging
from app.implementations import whoami
from inspect import currentframe

app_logger = logging.getLogger(f'ip-master.{__name__}')
app_logger.debug(f'Entering module {__name__}')


class GrpcServiceConnector(object):
    
    def __init__(self,service_class,config=None):
        app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

        if config == None:
            app_logger.error(f'Please specify a Server Config Object')
            return None
        
        server_address = config.get("SERVER")
        server_port = config.get("PORT")
        self._grpc_api_address = f'{server_address}:{server_port}'
        self._channel = None
        self._stub = None
        self._service_class = service_class

        app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')

    def start(self):
        app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
        import grpc

        self._channel = grpc.insecure_channel(self._grpc_api_address)
        self._stub = self._service_class(self._channel)

        app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')

    @property
    def stub(self):
        app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
        if self._stub is None:
            raise AttributeError(f'stub {self._service_class.__name__} is empty')


        app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')
        return self._stub

