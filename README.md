# mip-django

# install project
## First time
* docker-compose up -d
* docker-compose run app djang-admin startproject app .
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