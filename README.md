# Foodgram - Продуктовый Помощник
**Дипломный проект курса Бэкенд Разработки**

Foodgram - это онлайн-сервис, где пользователи могут публиковать рецепты, 
подписываться на других пользователей, добавлять рецепты в избранное и
список покупок, чтобы потом скачать список необходимых для приготовления
продуктов.

## Stack
* Python Django 3.1
* PostgreSQL
* Docker
* NGINX 

## Set up instructions:
* Install dependencies:
    * Docker 
        * https://docs.docker.com/engine/install/
    * Docker-Compose
        * https://docs.docker.com/compose/install/

* Clone the repo on your machien

* cd to the folder and fire it up
    * ```sudo docker-compose up --build```

* Apply migrations and load ingredients into the db
    * ```sudo docker-compose exec web python manage.py migrate```
    * ```sudo docker-compose exec web python manage.py loaddata ingredients.json```


[outdated] prod server ip: http://84.201.171.109/

[outdated] prod server url: http://plaun.ml/
