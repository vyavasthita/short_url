from concurrent import futures
import grpc
from grpc_connection import url_pb2
from grpc_connection import url_pb2_grpc
from django_grpc_framework import generics
from .models import Shortner
from .serializers import ShortProtoSerializer


class ShortService(generics.ModelService):
    def GetShortUrl(self, request, context):
        serializer = ShortProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        short = url_pb2.Short(short_url=request.long_url[0:21])
        serializer.save()
        # short = url_pb2.Short(short_url=request.long_url[0:21])
        # serializer = ShortProtoSerializer(short)
        return serializer.message
