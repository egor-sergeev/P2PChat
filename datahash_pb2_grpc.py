# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import datahash_pb2 as datahash__pb2


class DataHashStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.receive_message = channel.unary_unary(
                '/DataHash/receive_message',
                request_serializer=datahash__pb2.Text.SerializeToString,
                response_deserializer=datahash__pb2.Text.FromString,
                )


class DataHashServicer(object):
    """Missing associated documentation comment in .proto file"""

    def receive_message(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataHashServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'receive_message': grpc.unary_unary_rpc_method_handler(
                    servicer.receive_message,
                    request_deserializer=datahash__pb2.Text.FromString,
                    response_serializer=datahash__pb2.Text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataHash', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataHash(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def receive_message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataHash/receive_message',
            datahash__pb2.Text.SerializeToString,
            datahash__pb2.Text.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)