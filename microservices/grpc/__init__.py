import os
import sys

cwd = os.getcwd()
sys.path.append(os.path.join(cwd, "grpc_connection"))


from . import url_pb2, url_pb2_grpc
