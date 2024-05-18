import os
from modules import local_ip


os.system(f'python manage.py runserver {local_ip()}:8000')