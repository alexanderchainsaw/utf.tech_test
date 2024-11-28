# Тестовое задание `UTF.TECH`

## Перед запуском
 - Установить зависимости
 - Создать базу данных с необходимыми данными
   - `python manage.py migrate` 
   - `python manage.py loaddata db_data.json`

## Запуск
 - `python manage.py runserver`
 - Нужная ручка доступна по ссылке `http://127.0.0.1:8000/api/v1/foods/`
 - Чтобы запустить тесты данной ручки - `python manage.py test utf_tech\foods\`

## Структура
Интересующие нас файлы находятся в utf_tech/foods/
```
config
   |-- __init__.py
   |-- asgi.py
   |-- settings.py
   |-- urls.py
   |-- wsgi.py
manage.py
utf_tech
   |-- api
   |   |-- __init__.py
   |   |-- v1
   |   |   |-- __init__.py
   |   |   |-- apps.py
   |   |   |-- migrations
   |   |   |   |-- __init__.py
   |   |   |-- urls.py
   |-- foods
   |   |-- __init__.py
   |   |-- apis.py
   |   |-- apps.py
   |   |-- fixtures
   |   |   |-- test_foodlist_api
   |   |   |   |-- test_case_1
   |   |   |   |   |-- catalog_data.json
   |   |   |   |   |-- expected_response.json
   |   |   |   |-- test_case_2
   |   |   |   |   |-- ...
   |   |   |   |-- test_case_3
   |   |   |   |-- test_case_4
   |   |   |   |-- test_case_5
   |   |-- migrations
   |   |   |-- __init__.py
   |   |   |-- 0001_initial.py
   |   |-- models.py
   |   |-- selectors.py
   |   |-- serializers.py
   |   |-- tests
   |   |   |-- __init__.py
   |   |   |-- apis
   |   |   |   |-- __init__.py
   |   |   |   |-- test_foodlist.py
   |   |-- urls.py
```
