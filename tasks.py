import os

from invoke import run, task

from _project_.settings import DATA_DIR, STATIC_ROOT, MEDIA_ROOT, VENV_DIR

@task
def init():
    mkdir(DATA_DIR)
    mkdir(STATIC_ROOT)
    mkdir(MEDIA_ROOT)
    mkvenv(VENV_DIR, version='3.5')
    run(venv_activate_wrap('pip install -r requirements.txt', VENV_DIR))

@task
def runserver():
    run(venv_activate_wrap('python manage.py runserver', VENV_DIR), echo=True,
        pty=True)


def mkdir(path):
    if not os.path.exists(path):
        mkdir(os.path.dirname(path))
        os.mkdir(path)


def mkvenv(venv_path, version='3'):
    if os.name == 'nt':
        cmd = 'py -{0} -q -V'.format(version)
        r = run(cmd, warn=True)
        if not r.ok:
            raise RuntimeError('"{0}" do\'t work =/. Try reinstall Python or '
                               'check PATH environment variable'.format(cmd))
        return run("py -{0} -m venv {1}".format(version, venv_path))

    return run('virtualenv --python=python{1} "{0}"'
               .format(venv_path, version))


def venv_activate_wrap(cmd, path):
    venv_bin_path = os.path.join(path, 'bin')
    if os.name == 'nt':
        venv_bin_path = os.path.join(path, 'Scripts')

    active_path = os.path.normpath(os.path.join(venv_bin_path, 'activate'))
    wrapped_cmd = '. ' + active_path + " && " + cmd
    if os.name == 'nt':
        wrapped_cmd = active_path + ' && ' + cmd
    return "({})".format(wrapped_cmd)
