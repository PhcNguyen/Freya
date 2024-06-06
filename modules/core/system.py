import os
import sys
import time
import socket
import shutil
import pathlib
import os.path
import requests
import subprocess

from typing import NoReturn, Union
from .utils import Colors, FRAMES, MESSAGE


class Terminal:
    Windows = os.name == 'nt'

    @staticmethod
    def Clear() -> int:
        return os.system("cls" if Terminal.Windows else "clear")

    @staticmethod
    def Title(title: str) -> int:
        if Terminal.Windows:
            return os.system(f"title {title}")

    @staticmethod
    def Size(x: int, y: int) -> int:
        if Terminal.Windows:
            return os.system(f"mode {x}, {y}")
        
    @staticmethod
    def Command(command: str) -> int:
        return os.system(command)

    @staticmethod
    def Reset() -> NoReturn:
        os.execv(sys.executable, ['python'] + sys.argv)

    @staticmethod
    def Exit() -> NoReturn:
        sys.exit()

    @staticmethod
    def Console(title: str, color: str, message: str) -> bool:
        white = Colors.White
        try:
            msg = str(message)
            colors = getattr(Colors, color)
            print(MESSAGE.format(title, colors, msg))
            return True
        except Exception as error:
            raise error
    
    @staticmethod
    def Sleep(times: int) -> None:
        for i in range(times, 0, -1):
            for frame in FRAMES:
                sys.stdout.write(f'{frame}[{Colors.Orange}{i:02}{Colors.White}]')
                sys.stdout.flush()
                time.sleep(0.125)
        sys.stdout.write('\r')


class System:
    @staticmethod
    def remove_pycahe() -> None:
        for root, dirs, files in os.walk(pathlib.Path.cwd()):
            for dir_name in dirs:
                if dir_name == "__pycache__":
                    pycache_dir = os.path.join(root, dir_name)
                    shutil.rmtree(pycache_dir)
            for file_name in files:
                if file_name.endswith(".pyc") or file_name.endswith(".pyo"):
                    pyc_file = os.path.join(root, file_name)
                    os.remove(pyc_file)
    
    @staticmethod
    def local_ip() -> Union[str, dict]:
        try:
            with socket.socket() as dns:
                dns.connect(("8.8.4.4", 80))
                return dns.getsockname()
        except Exception as error:
            raise error


def Github():
    start = time.time()
    Terminal.Clear()

    try:
        response = requests.get('https://github.com')
        if response.status_code == 200:
            Terminal.Console('Ping', 'Orange', 'Connect to "github.com" successful')
        else:
            Terminal.Console('Ping', 'Red', f'Error: HTTP status code {response.status_code}')
            Terminal.Exit()
    except Exception as e:
        Terminal.Console('Ping', 'Red', str(e))
        Terminal.Exit()

    try:
        with open('.github/.version', 'r') as file:
            __version__ = file.read().strip()
    except FileNotFoundError:
        Terminal.Console('GitHub', 'Red', 'File ".version" not found')
        Terminal.Exit()
    except Exception as e:
        Terminal.Console('GitHub', 'Red', f'Error reading ".version" file: {e}')
        Terminal.Exit()

    try:
        commands = [
            (['git', 'add', '.'], 'git add .'),
            (['git', 'commit', '-m', __version__], f'git commit -m "{__version__}"'),
            (['git', 'push', 'origin', 'main'], 'git push origin main')
        ]
        
        for command, msg in commands:
            subprocess.run(command, stdout=-3, stderr=-3)
            Terminal.Console('GitHub', 'Blue', msg)

        elapsed_time = time.time() - start
        Terminal.Console('Timer', 'Yellow', f'Elapsed time for push: {elapsed_time:.2f} seconds')
    except FileNotFoundError:
        Terminal.Console('GitHub', 'Red', 'Git command not found')
        Terminal.Exit()
    except Exception as e:
        Terminal.Console('GitHub', 'Red', f'Error executing Git command: {e}')
        Terminal.Exit()
