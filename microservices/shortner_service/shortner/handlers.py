from grpc_connection import url_pb2_grpc
from .service import ShortService


def grpc_handlers(server):
    url_pb2_grpc.add_UrlShortnerServicer_to_server(ShortService.as_servicer(), server)