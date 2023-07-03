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

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install mysqlclient

ARG DB_TYPE=MYSQL
ENV DB_TYPE=${DB_TYPE}

COPY ./apps /app/apps
COPY ./migrations /app/migrations
COPY ./utils /app/utils
COPY entrypoint.sh .
COPY wsgi.py .

# Copy files for unit tests
COPY ./tests /app/tests
COPY pytest.ini .
COPY .coveragerc .

# Copy grpc related files
COPY ./grpc_client /app/grpc_client

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
