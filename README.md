# Django_AutomationTestFramework
AutomationTestFramework on Django

Require lib:
1. Install Django:
    pip install django
3. Install Python3

Currently use default Django sqlite as backend.May switch to other sql in future.

Create Django project:
    django-admin startproject [project name]

Start App:
    python manage.py startapp [appname]

Running server:
    python manage.py runserver [set IP and port](optional) (default: 127.0.0.1:8000/)

Database migrate:
    python manage.py migrate

Create admin:
    python manage.py superuser

Enter Django shell:
    python manage.py shell