#!/bin/bash
source ~/.virtualenvs/olimpiadas/bin/activate
./manage.py makemigrations
./manage.py migrate
./manage.py init
./populate-database/script.sh
./populate-database/script.sh
