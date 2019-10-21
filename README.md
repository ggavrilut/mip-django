# mip-django

# install project
## First time
* docker-compose up -d
* docker-compose run app django-admin startproject app .

#### To use mongodb with Django
* install djongo *see requirements.txt* with a specific value for **sqlparse**
* create database in mongo for the project
* configure in settings.py

##### After project installation regain right with command 
* sudo chown -R $USER:$USER .

## Project exists
* docker-compose up -d

# Run project
* docker-compose up -d
* docker-compose stop

### Enter in project
*  docker-compose exec app bash

# Apply changes of configuration
_in **requirements.txt** or in **Dockerfile** or **docker-compose.yml**_
* docker-compose build
* docker-compose down
* docker-compose up -d

# Useful commands
## Persist database changes
* python manage.py makemigrations
* python manage.py migrate
## Create module
* python manage.py startapp
## Create superuser
* python manage.py createsuperuser