# Init new project

    # prepare
    pip install invoke
    pip install virtualenv
    pip install wheel

    # initialization
    invoke init


# init db

    invoke r "python manage.py migrate"
