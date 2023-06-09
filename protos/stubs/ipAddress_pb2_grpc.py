# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.protos.stubs.ipAddress_pb2 as ipAddress__pb2


class IpAddressStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetIpAddressById = channel.unary_unary(
                '/dbAccess.IpAddress/GetIpAddressById',
                request_serializer=ipAddress__pb2.IpAddressIdRequest.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.GetIpAddressByName = channel.unary_unary(
                '/dbAccess.IpAddress/GetIpAddressByName',
                request_serializer=ipAddress__pb2.IpAddressNameRequest.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.GetIpAddressBySubnet = channel.unary_unary(
                '/dbAccess.IpAddress/GetIpAddressBySubnet',
                request_serializer=ipAddress__pb2.IpAddressSubnetRequest.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.AddIpAddress = channel.unary_unary(
                '/dbAccess.IpAddress/AddIpAddress',
                request_serializer=ipAddress__pb2.ipAddress.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.UpdateIpAddress = channel.unary_unary(
                '/dbAccess.IpAddress/UpdateIpAddress',
                request_serializer=ipAddress__pb2.ipAddress.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.DeleteIpAddressById = channel.unary_unary(
                '/dbAccess.IpAddress/DeleteIpAddressById',
                request_serializer=ipAddress__pb2.IpAddressIdRequest.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )
        self.DeleteIpAddressByName = channel.unary_unary(
                '/dbAccess.IpAddress/DeleteIpAddressByName',
                request_serializer=ipAddress__pb2.IpAddressNameRequest.SerializeToString,
                response_deserializer=ipAddress__pb2.IpAddressResponse.FromString,
                )


class IpAddressServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetIpAddressById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIpAddressByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIpAddressBySubnet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddIpAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateIpAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIpAddressById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIpAddressByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IpAddressServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetIpAddressById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIpAddressById,
                    request_deserializer=ipAddress__pb2.IpAddressIdRequest.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'GetIpAddressByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIpAddressByName,
                    request_deserializer=ipAddress__pb2.IpAddressNameRequest.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'GetIpAddressBySubnet': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIpAddressBySubnet,
                    request_deserializer=ipAddress__pb2.IpAddressSubnetRequest.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'AddIpAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.AddIpAddress,
                    request_deserializer=ipAddress__pb2.ipAddress.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'UpdateIpAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateIpAddress,
                    request_deserializer=ipAddress__pb2.ipAddress.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'DeleteIpAddressById': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteIpAddressById,
                    request_deserializer=ipAddress__pb2.IpAddressIdRequest.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
            'DeleteIpAddressByName': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteIpAddressByName,
                    request_deserializer=ipAddress__pb2.IpAddressNameRequest.FromString,
                    response_serializer=ipAddress__pb2.IpAddressResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dbAccess.IpAddress', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IpAddress(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetIpAddressById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dbAccess.IpAddress/GetIpAddressById',
            ipAddress__pb2.IpAddressIdRequest.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIpAddressByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dbAccess.IpAddress/GetIpAddressByName',
            ipAddress__pb2.IpAddressNameRequest.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIpAddressBySubnet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dbAccess.IpAddress/GetIpAddressBySubnet',
            ipAddress__pb2.IpAddressSubnetRequest.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddIpAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dbAccess.IpAddress/AddIpAddress',
            ipAddress__pb2.ipAddress.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateIpAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dbAccess.IpAddress/UpdateIpAddress',
            ipAddress__pb2.ipAddress.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteIpAddressById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dbAccess.IpAddress/DeleteIpAddressById',
            ipAddress__pb2.IpAddressIdRequest.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteIpAddressByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dbAccess.IpAddress/DeleteIpAddressByName',
            ipAddress__pb2.IpAddressNameRequest.SerializeToString,
            ipAddress__pb2.IpAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
