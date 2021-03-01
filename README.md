# Foodgram - Продуктовый Помощник
**Дипломный проект курса Бэкенд Разработки**

Foodgram - это онлайн-сервис, где пользователи могут публиковать рецепты, 
подписываться на других пользователей, добавлять рецепты в избранное и
список покупок, чтобы потом скачать список необходимых для приготовления
продуктов.

## Стэк
* Python Django 3.1
* PostgreSQL
* Docker
* NGINX 

## Запуска проекта
* Установите зависимости 
    * Docker 
        * https://docs.docker.com/engine/install/
    * Docker-Compose
        * https://docs.docker.com/compose/install/

* Склонируйте репозиторий на локальную машину или сервер

* Переключитесь в папку приложения и разверните проект
    * ```sudo docker-compose up --build```

* Выполните миграции и загрузите список ингредиентов в базу
    * ```sudo docker-compose exec web python manage.py migrate```
    * ```sudo docker-compose exec web python manage.py loaddata ingredients.json```


prod server ip: http://84.201.171.109/

prod server url: http://plaun.ml/