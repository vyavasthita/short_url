#!/bin/bash


echo "generate grpc files"
python -m grpc_tools.protoc -I ./grpc_client/protobufs --python_out=./grpc_client --pyi_out=./grpc_client --grpc_python_out=./grpc_client ./grpc_client/protobufs/url.proto

echo "Migrate the Database"

# Run flask migrate
echo "Run flask migrate"
flask db migrate

echo 2

# Upgrade db
echo "Run db upgrade"
flask db upgrade

# Run flask server
echo "Run web server"
gunicorn -c apps/config/gunicorn_conf.py wsgi
