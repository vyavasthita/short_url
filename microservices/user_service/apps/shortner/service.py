import grpc
from grpc_connection import url_pb2
from grpc_connection import url_pb2_grpc
from apps import configuration
from utils.response import Response


class ShortnerService:
    def get_short_url(self, long_url: str):
        # Create a Channel
        with grpc.insecure_channel(
            f"{configuration.SHORTNER_SERVICE_HOST}:{configuration.SHORTNER_SERVICE_PORT}"
        ) as channel:
            # Create a Stub
            stub = url_pb2_grpc.UrlShortnerStub(channel)

            # Call Api
            long = url_pb2.Long(long_url=long_url)
            response = stub.GetShortUrl(long)

        return Response(result=response.short_url)



