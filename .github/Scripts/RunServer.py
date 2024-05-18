import os.path
from sys import exit, path
path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os
from modules import local_ip


os.system(f'python manage.py runserver {local_ip()}:8000')