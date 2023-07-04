#!/bin/sh

echo "generate grpc files"
python -m grpc_tools.protoc -I ./grpc_connection/protobufs --python_out=./grpc_connection --pyi_out=./grpc_connection --grpc_python_out=./grpc_connection ./grpc_connection/protobufs/url.proto

echo "Running makemigrations"
python manage.py makemigrations shortner

echo "Running migrate"
python manage.py migrate

# echo "Create Super User"
# python manage.py createsuperuser --no-input --username admin --email admin@admin.com

echo "Running django server"
# python manage.py grpcrunserver 0.0.0.0:5003
python manage.py grpcrunserver --dev
