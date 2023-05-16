import logging
logger = logging.getLogger(f'ip-master.{__name__}')


from inspect import currentframe
from app.implementations import whoami

from app.protos import ipAddress_pb2_grpc as ip_grpc
from app.protos import ipAddress_pb2 as ip_pb2

class IpAddressServicer(ip_grpc.IpAddressServicer):

    def __init__(self):
        return
    
    def _convert_db_row_to_grpc_message(ip):
        return
    
    def GetIpAddressById(self, request, context):
        logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
        logger.debug(f'request = {request}')
        logger.debug(f'Request Type = {type(request)}')
        logger.debug(f'request.id = {getattr(request,"id",None)}')
        logger.debug(f'request.name = {getattr(request,"name",None)}')

        from app.implementations.ipAddress import getIpAddress
        ip = getIpAddress(request,context)
        
        logger.debug(f'Returned IP = {ip}')
        logger.debug(f'Type = {type(ip)}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return ip_pb2.IpAddressResponse(ipAddress=ip)


    def GetIpAddressByName(self, request, context):
        logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

        from app.implementations.ipAddress import getIpAddress
        ip = getIpAddress(request,context)
        logger.debug(f'Returned IP = {ip}')
        logger.debug(f'Type = {type(ip)}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return ip_pb2.IpAddressResponse(ipAddress=ip)


    def GetIpAddressBySubnet(self, request, context):
        logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

        from app.implementations.ipAddress import getIpAddress
        ip = getIpAddress(request,context)
        logger.debug(f'Returned IP = {ip}')
        logger.debug(f'Type = {type(ip)}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return ip_pb2.IpAddressResponse(ipAddress=ip)


def serve(server):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    logger.info(f'Adding the ipAddress Servicer to the GRPC Server')
    ip_grpc.add_IpAddressServicer_to_server(IpAddressServicer(),server)
    
    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return server

