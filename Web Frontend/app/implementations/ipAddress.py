import logging
from app.implementations import whoami
from inspect import currentframe

app_logger = logging.getLogger(f'ip-master.{__name__}')
app_logger.debug(f'Entering module {__name__}')

import grpc

class ipAddressClient(object):

    def __init__(self,config):
        app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

        from app.implementations.grpc_service_connector import GrpcServiceConnector
        from app.protos import ipAddress_pb2_grpc

        self.ipAddress_conn = GrpcServiceConnector(ipAddress_pb2_grpc.IpAddressStub,config)
        self.ipAddress_conn.start()

        app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')


    def get_ip_address(self,name=None,subnet=None,id=None):
        app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

        from app.protos import ipAddress_pb2
        if id != None:
            try:
                app_logger.debug(f'Setting up gRPC Request')
                req = ipAddress_pb2.IpAddressIdRequest(id=id)
                app_logger.debug(f'Req = {req}')
                app_logger.debug(f'Req Type = {type(req)}')
                app_logger.debug(f'Request created - Sending for response')
                res = self.ipAddress_conn.stub.GetIpAddressById(req)
                app_logger.debug(f'gRPC Response Received')
                app_logger.debug(res)
            except Exception as e:
                app_logger.error(type(e))
                app_logger.error(f'Error: {e}',exc_info=True)
                return f'Could not find a row with id {id}'
        elif name != None:
            pass
        elif subnet != None:
            pass
        else:
            app_logger.error(f'Please provide an ID, Name or Subnet with which to find an IP')
            return None
        

        app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')
        return res        



