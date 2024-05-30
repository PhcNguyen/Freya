import os
import subprocess
from modules.core.utils import localIP

PORT = 8000


def run_server():
    SERVER = f"{localIP}:{PORT}"
    command = '{} manage.py runserver' + SERVER
    if os.name == 'nt':
        command = command.format('python')
    else:
        command = command.format('python3')
    subprocess.Popen(command, shell=True) 


if __name__ == '__main__':
    run_server()
