FROM python:3.8.5-alpine3.12
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev libjpeg jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev libffi-dev make py-gevent libressl-dev libc-dev build-base
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /app
COPY docker-run.sh /code/docker-run.sh
WORKDIR /app
CMD ./docker-run.sh