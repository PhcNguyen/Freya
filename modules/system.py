import sys
import time
import os.path
import requests
import subprocess

from socket import socket, AF_INET, SOCK_DGRAM
from typing import NoReturn, Any
from modules.style import Colors
from modules.utils import FRAMES, MESSAGE, VERSION



class System:
    """
    6 functions: 
    - clear()   |   Clears the terminal screen
    - command() |   Executes a system command
    - reset()   |   Resets the Python script by re-executing it
    - exit()    |   Exits the Python script
    - console() |   Prints a formatted message to the console
    - sleep()   |   Shows a countdown with a specified number of frames
    """
    Windows = os.name == 'nt'

    @staticmethod
    def init() -> int:
        os.system('')

    @staticmethod
    def clear() -> int:
        return os.system(
            "cls" if System.Windows else "clear"
        )
        
    @staticmethod
    def command(command: str) -> int:
        return os.system(command)

    @staticmethod
    def reset() -> NoReturn:
        return os.execv(
            sys.executable, ['python'] + sys.argv
        )

    @staticmethod
    def exit() -> NoReturn:
        sys.exit()

    @staticmethod
    def console(name: str, color: str, message: str) -> None:
        print(MESSAGE.format(name, getattr(Colors, color.lower()), str(message)))

    @staticmethod
    def sleep(times: int) -> None:
        for i in range(times, 0, -1):
            for frame in FRAMES:
                sys.stdout.write(f'{frame}[{Colors.Orange}{i:02}{Colors.White}]')
                sys.stdout.flush()
                time.sleep(0.125)
        sys.stdout.write('\r')   

    @staticmethod
    def localIP() -> Exception | Any:
        try:
            with socket(AF_INET, SOCK_DGRAM) as dns:
                dns.connect(("8.8.4.4", 80))
                return dns.getsockname()[0]
        except Exception as error:
            return error



class Github:
    start = time.time()

    @staticmethod
    def end():
        System.console(
            'Timer', 'Yellow',
            f'Elapsed time for push: {(time.time() - Github.start):.2f} seconds'
        )
        System.exit()

    @staticmethod
    def ping(url: str) -> bool:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                System.console('Ping', 'Orange', 'Connect to "github.com" successful')
                return True
            else:
                System.console('Ping', 'Red', f'Error: HTTP status code {response.status_code}')
                return False
        except Exception as e:
            System.console('Ping', 'Red', str(e))
            return False

    @staticmethod
    def command(command, message) -> None:
        try:
            subprocess.run(command, -1, None, None, -3, -3)
            System.console('GitHub', 'Blue', message)
        except FileNotFoundError:
            System.console('GitHub', 'Red', 'Git command not found')
            Github.end()
        except Exception as e:
            System.console('GitHub', 'Red', f'Error executing Git command: {e}')
            Github.end()

    @staticmethod
    def automatic() -> None:
        if not Github.ping('https://github.com'):
            Github.end()

        commands = [
            (['git', 'add', '.'], 'git add .'),
            (['git', 'commit', '-m', VERSION], f'git commit -m "{VERSION}"'),
            (['git', 'push', 'origin', 'main'], 'git push origin main')
        ]
        for command in commands:
            Github.command(command[0], command[1])

        Github.end()