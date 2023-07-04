#!/bin/bash


echo "generate grpc files"
python -m grpc_tools.protoc -I ./grpc_connection/protobufs --python_out=./grpc_connection --pyi_out=./grpc_connection --grpc_python_out=./grpc_connection ./grpc_connection/protobufs/url.proto

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
