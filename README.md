# mip-django

# install project
## First time
* docker-compose up -d
* docker-compose run app django-admin startproject app .

#### To use mongodb with Django
* install djongo *see requirements.txt* with a specific value for **sqlparse**
* create database in mongo for the project
* configure in settings.py

## Project exists
* docker-compose up -d

# Run project
* docker-compose up -d
* docker-compose stop

# Apply changes
_in **requirements.txt** or in **Dockerfile** or **docker-compose.yml**_
* docker-compose build
* docker-compose down
* docker-compose up -d