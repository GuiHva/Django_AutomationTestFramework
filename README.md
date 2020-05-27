# Django_AutomationTestFramework
AutomationTestFramework on Django

Require lib:
1. Install Python3
2. Install Django3:
    pip install django3
3. Install Django-Bootstrap3
    pip install django-bootstrap3

Notice:
    I commented csrf_auth due to this repo just my autoframework dev test repo,
    I will never put it online, don't remove csrf_auth if you want to deploy your own website.

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

Start Test:
    python manage.py test [testmodule](optional)

Provided API

|API| URL | request way|
|:---|:---|:---|
|Add event      | http://127.0.0.1:8000/api/add_event/ | POST |
|get event list | http://127.0.0.1:8000/api/get_event_list/ | GET |
|add_guest      | http://127.0.0.1:8000/api/add_guest/ | POST |
|get guest list | http://127.0.0.1:8000/api/get_guest_list/ | GET |
|guest sign     | http://127.0.0.1:8000/api/user_sign/ | GET |