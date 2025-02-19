#!/bin/bash

python manage.py migrate && \
python manage.py load_users_and_groups && \
python manage.py load_mypedia  && \
python manage.py runserver 0.0.0.0:8000