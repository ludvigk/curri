# curri
[![Build Status](https://travis-ci.org/ludvigk/curri.svg?branch=master)](https://travis-ci.org/ludvigk/curri)
[![Issue Count](https://codeclimate.com/github/ludvigk/curri/badges/issue_count.svg)](https://codeclimate.com/github/ludvigk/curri)


SurveyBot for feedback and suggestions for exercises in lectures. Project for TDT4140.

## Requirements
* Python3
* RabbitMQ-server

## Installation Guide

1. Download the source code.
2. Install the required software.

    **With macOS/Homebrew**
    ```zsh
        $ brew install python3
        $ brew install rabbitmq
    ```
    **With apt-get**
    ```zsh
        $ apt-get install python3
        $ apt-get install rabbitmq-server
    ```
3. Install required python modules from curri/
    ```zsh
        $ pip3 install -r requirements.txt
    ```
4. Create *email_settings.py* file in *curri/mysite/mysite/*
    ```python
        EMAIL_USE_TLS = True
        EMAIL_HOST = 'smtp.example.com'
        EMAIL_HOST_USER = 'email@example.com'
        EMAIL_HOST_PASSWORD = 'password'
        EMAIL_PORT = 587
    ```
5. Add *mysite_uwsgi.ini* file to *curri/mysite/*
    ```ini
        # mysite_uwsgi.ini file
        [uwsgi]
        
        # Django-related settings
        # the base directory (full path)
        chdir           = # TODO
        
        # Django's wsgi file
        module          = mysite.wsgi
        
        # the virtualenv (full path)
        # ignore if not using virtualenv
        home            = # TODO
        
        # process-related settings
        # master
        master          = true
        
        # maximum number of worker processes
        processes       = 10
        
        http-socket     = [::]:80
        vacuum          = true
    ```
6. Migrate databases in *curri/mysite*
    ```zsh
        $ python3 manage.py migrate
    ```
6. Start Celery and RabbitMQ in their own terminal
    ```zsh
        $ sudo rabbitmq-server
    ```
    ```zsh
        $ celery -A mysite worker -l info
    ```
7. Run the server
    ```zsh
        $ cd curri/mysite/
        $ sudo uwsgi --ini mysite_uwsgi.ini
    ```
