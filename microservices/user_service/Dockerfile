FROM python:3.8.16-alpine3.18

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

WORKDIR /app

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

EXPOSE 5001

COPY ./user_service/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install mysqlclient

ARG DB_TYPE=MYSQL
ENV DB_TYPE=${DB_TYPE}

# Copy grpc related files
COPY ./grpc /app/grpc_connection

COPY ./user_service/apps /app/apps
COPY ./user_service/migrations /app/migrations
COPY ./user_service/utils /app/utils
COPY ./user_service/docker-entrypoint.sh .
COPY ./user_service/wsgi.py .

# Copy files for unit tests
COPY ./user_service/tests /app/tests
COPY ./user_service/pytest.ini .
COPY ./user_service/.coveragerc .

RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
