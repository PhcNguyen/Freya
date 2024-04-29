from subprocess import run


run(['python', 'manage.py', 'migrate'])

run(['python', 'manage.py', 'runserver'])