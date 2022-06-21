<h1 align="center"> Conecte Estudo: Plataforma Web para Auxílio no Ensino à Distância </h1>

[Conecte Estudo](https://github.com/igor-rufino/webapp-ead) is a web application to aid distance learning, which includes a virtual agenda for the user.
For the student, it is a place where he can control his schedule, view his tasks and/or insert a new one, thinking about the practicality and routines to control and help his tasks.
For the teacher, it is a place where he can set up his classes, create tasks, execute teaching plans and class materials, as well as being able to control his own schedule and create activities for himself.

This project contains the REST API, developed using the Django framework, to connect the web application, developed in React, to the MongoDB database.

## Topics 
- [Pre-Requisites](#pre-requisites-) 
- [Authors](#authors)
- [Steps to implementation](#steps-to-implementation-)
- [Steps to implementation](#steps-to-implementation-)
- [Instalation](#instalation-)

## Pre-Requisites 📋
- python3
- Django
- Djongo
- Djoser
- MongoDB

## Authors
* **Ana Luiza Silva Terra** - [Ana Luiza](https://github.com/analuizat3)
* **Igor Rufino Ribeiro** - [Igor](https://github.com/igor-rufino)
* **Paulo Gabriel de Freitas Rotundaro** - [Paulo](https://github.com/PauloRotundaro)
* **Pedro Abritta Reis** - [Pedro](https://github.com/pedro-toodoo)

## Steps to implementation 🏃

### Django REST Framework implementation: 
<h5>Creating apps:</h5>

```
django-admin startapp nameapp
```

<h5>Make tables migrations to database: </h5>

```
python manage.py makemigrations
python manage.py migrate
```

<h5>Start local server: </h5>

```
python manage.py runserver
```

### Creating a database on MongoDB<a href="https://www.mongodb.com/pt-br/products/compass"> Compass </a>:
<h5>You can create local variables like DB_USERNAME and DB_PASSWORD or just put the user in the URL to make the connection: </h5>
<h5> Note: we have a constant.py file with DB_USERNAME, DB_PASSWORD and DJANGO_Key, you should create the same and put your own user and key. </h5>
<h5> On Settings.py you just import constant and use it. </h5>

![image](https://user-images.githubusercontent.com/94690905/174868977-adb65a53-58a8-4197-bca1-47b53a62be82.png)


## Instalation 🔧
- Easy instalation: install libs from 'requirements.txt':
```
pip install -r requirements.txt
```
- Or you can install lib by lib specified in the requirements:
```
pip install [lib_name]
```
