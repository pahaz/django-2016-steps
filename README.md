# FILES

 - `_project_` - django project directory
 - `__data__` - db, media, and collected static files directory
 - `run.sh` - run command in virtualenv (helper)
 - `tasks.py` - invoke file

# Workflow

    # prepare
    pip install invoke
    pip install virtualenv
    pip install wheel

    # initialization
    invoke init

    # init db
    invoke migrate
    ./run.sh python manage.py createsuperuser

    # create app
    ./run.sh python manage.py startapp <name>

    # runserver
    invoke runserver


# poll

 - /poll/

# code

 - /code/
