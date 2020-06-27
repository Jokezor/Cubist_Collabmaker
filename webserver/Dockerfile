# pull official base image
FROM python:3.8.2

# set work directory
WORKDIR /usr/src/webserver

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# To have same settings
ENV DJANGO_SETTINGS_MODULE mysite.settings

# Install netcat which is used in entrypoint.sh with command: nc
RUN apt-get update && apt-get install -y netcat

# update and add support for psycopg2, only needed for alpine version of python
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Install postgis needed for postgresql geo data handling
#RUN apt-get install -y postgis:3.0.0

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/webserver/requirements.txt
RUN pip install -r requirements.txt

# Install gdal for geodjango
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin


# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/webserver/entrypoint.sh

# copy project
COPY . /usr/src/webserver/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/webserver/entrypoint.sh"]


