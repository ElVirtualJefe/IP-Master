import logging
logger = logging.getLogger(f'ip-master.{__name__}')


from inspect import currentframe
from app.implementations import whoami

from app.protos.stubs import ipAddress_pb2_grpc as ip_grpc

class IpAddressServicer(ip_grpc.IpAddressServicer):

    def __init__(self):
        return
    
    def _convert_db_row_to_grpc_message(ip):
        return
    
    def GetIpAddressById(self, request, context, session):
        logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

        from ipAddress import _getIpAddressById
        ip = _getIpAddressById(request.id)
        logger.debug(f'Returned IP = {ip}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return super().GetIpAddressById(request, context)


def serve(server):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    logger.info(f'Adding the ipAddress Servicer to the GRPC Server')
    ip_grpc.add_IpAddressServicer_to_server(IpAddressServicer(),server)
    
    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return server

