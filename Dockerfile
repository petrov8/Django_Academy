FROM python:3.8

RUN apt update -y \
    && apt upgrade -y


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#deploy from this app
ENV HOME=/home/app

# image folder / deploy folder
ENV APP_HOME=/home/app/web

# change to and if it doesn't exist - create
WORKDIR $APP_HOME

RUN pip install --upgrade pip

# copy requirements inside WORKDIR
COPY requirements.txt requirements.txt

# install copies requirements
RUN pip install -r requirements.txt

# copy all files from my project folder to image
COPY . .


