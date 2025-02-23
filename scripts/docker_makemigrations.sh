# !/bin/bash

docker-compose exec web python manage.py makemigrations
sleep 0.2
docker-compose exec web python manage.py migrate