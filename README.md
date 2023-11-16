# short_url

python -m grpc_tools.protoc -I../protos --python_out=../grpc_generated --pyi_out=../grpc_generated --grpc_python_out=. ../protos/url.proto

python -m grpc_tools.protoc -I ./protobufs --python_out=./grpc_generated --pyi_out=./grpc_generated --grpc_python_out=./grpc_generated ./protobufs/url.proto

python -m grpc_tools.protoc -I ./protobufs --python_out=. --pyi_out=. --grpc_python_out=. ./protobufs/url.proto