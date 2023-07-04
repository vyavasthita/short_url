from django_grpc_framework import proto_serializers
from grpc_connection import url_pb2
from grpc_connection import url_pb2_grpc
from .models import Shortner


class ShortProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Shortner
        proto_class = url_pb2.Short
        fields = ["id", "long_url", "short_url"]
