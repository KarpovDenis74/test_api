# [***«Тестовый проек test_API»»***](http://github.com/KarpovDenis74/test_api.git)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

#### [Требования к проекту]

----
    Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: Django 2.2.10, Django REST framework.
----

## [Запуск проекта]

### [Вариант 1 - Запуск на локальной машине]
1. Клонируйте данный репозиторий к себе в папку:
    ```
        git clone htth://github.com/KarpovDenis74/test_api.git
    ```
2. Создайте виртуальное окружение 
    ```
        python3 -m venv venv
    ```
3. Активируйте виртуальное окружение 
    ```
        source venv/bin/activate            # Для Mac OS
        source venv/Scripts/activate        # Для Windows
    ```
4. Установите зависимости
    ```
        pip install -r requirements.txt
    ```
5 Примените миграции, введите:  
    ```
        python manage.py migrate --noinput
    ```
6 Создайте суперпользователя, необходимо ввести:  
    ```
        python manage.py createsuperuser
    ```
7 Собирите статику:  
    ```
        python manage.py collectstatic --noinput
    ```
Вы великолепны :) Проект запущен !!!


### [Вариант 2 - Запуск в контейнере]
1 Скопируйте в рабочую директорию:
    ```
        DockerFile
    ```
2 Создайте файл .env и заполните его своими значениями. 
    Все нужные переменные описаны файле 
        ```
            .env.template
        ```
3 Запустите контейнер (doker скачает образ test_api с ресурса DockerHub и запустит контейнер):  
    ```
        docker run -it -p 8000:8000 test_api
    ```
4 Зайдите в контейнер:
     ```
        docker exec -it <CONTAINER ID> bash 
    ```
    4.1 Примените миграции, введите:  
        ```
            python code/ manage.py migrate --noinput
        ```
    4.2 Создайте суперпользователя, необходимо ввести:  
        ```
            python code/manage.py createsuperuser
        ```
    4.3 Собирите статику:  
        ```
            python code/manage.py collectstatic --noinput
        ```
5 В браузере в адресной строке наберите
    ```
        localhost:8000
    ```
Вы великолепны :) Проект запущен !!!
   
## [Технологии]
-------------
* [Python](https://www.python.org/) - высокоуровневый язык программирования общего назначения;
* [Django](https://www.djangoproject.com/) - фреймворк для веб-приложений;
* [Django REST framework](https://www.django-rest-framework.org/) - API фреймворк для Django;
* [PostgreSQL](https://www.postgresql.org/) - объектно-реляционная система управления базами данных;
* [Nginx](https://nginx.org/) - HTTP-сервер и обратный прокси-сервер, почтовый прокси-сервер, а также TCP/UDP прокси-сервер общего назначения;
* [Docker](https://www.docker.com/) - ПО для автоматизации развёртывания и управления приложениями в средах с поддержкой контейнеризации;
* [Docker-Compose](https://docs.docker.com/compose/) - инструмент для создания и запуска многоконтейнерных Docker приложений. 