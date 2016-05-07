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
