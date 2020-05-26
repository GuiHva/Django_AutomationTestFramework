# Django_AutomationTestFramework
AutomationTestFramework on Django

Require lib:
1. Install Python3
2. Install Django3:
    pip install django3
3. Install Django-Bootstrap3
    pip install django-bootstrap3

Currently use default Django sqlite as backend.May switch to other sql in future.
Frontend:
    Bootstrap3
Backend:
    sqlite

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