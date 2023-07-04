FROM python:3.11.3-alpine3.18

WORKDIR /app
EXPOSE 5003

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY ./shortner_service/requirements.txt .

RUN pip install -r requirements.txt
RUN pip install mysqlclient

# Copy grpc related files
COPY ./grpc /app/grpc_connection

COPY ./shortner_service/shortner_service /app/shortner_service
COPY ./shortner_service/shortner /app/shortner

COPY ./shortner_service/manage.py .
COPY ./shortner_service/docker-entrypoint.sh .

RUN chmod +x docker-entrypoint.sh

ARG DJANGO_SUPERUSER_PASSWORD
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]