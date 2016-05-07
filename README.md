# FILES

 - `_project_` - django project directory
 - `__data__` - db, media, and collected static files directory
 - `run.sh` - run command in virtualenv (helper)
 - `tasks.py` - invoke file

# Init new project

    # prepare
    pip install invoke
    pip install virtualenv
    pip install wheel

    # initialization
    invoke init


# Init db

    invoke migrate
    ./run.sh python manage.py createsuperuser

# Create app

    ./run.sh python manage.py startapp <name>

# STEPS #

## Step 1 ##

 - `virtualenv`, activate, `pip install -r requirements.txt`
 - `invoke`: `invoke.run` and `invoke.task`
 - start new django project by `startproject`
 - project structure (`manage.py`, `_project`, `_project/settings.py`, `_project/wsgi.py`, `_project_/urls.py`)
 - project settings (`DEBUG`, `INSTALLED_APPS`, `ROOT_URLCONF`, `WSGI_APPLICATION`, `DATABASES`, `TEMPLATES`)
 - `migrate`, `createsuperuser`, `python manage.py runserver`
 - write simple view `def index(request): return render(request, 'index.html')` in `urls.py`
 - add `_project__/templates/index.html` and `_project__/templates/base.html`
 - install `django_debug_toolbar`, `django_extensions`, add to `INSTALLED_APPS`
 - show `debug-toolbar` features
 - show `python manage.py runserver_plus`
 - add static file `_project_/static/robots.txt`, change settings `STATICFILES_DIRS`; tell about how django serve static files, `'django.contrib.staticfiles'`
 - show django admin interface; tell about `User`, `Group`, and `Permission` models; overview of `INSTALLED_APPS`
 - `startapp` and include urls.py (`./run.sh python manage.py startapp <name>`)
