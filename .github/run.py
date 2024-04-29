import sys
import os.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from subprocess import run


run(['python', 'manage.py', 'migrate'])
run(['python', 'manage.py', 'runserver'])