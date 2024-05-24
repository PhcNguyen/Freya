import os.path
from sys import path
path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import requests
from subprocess import run, DEVNULL



class Col:
    @staticmethod
    def start(color: str) -> str:
        return f"\033[38;2;{color}m"
    
    Red    = start('255;0;0'    )
    Blue   = start('28;121;255' )
    Cyan   = start('0;255;255'  )
    Pink   = start('255;192;203')
    Black  = start('0;0;0'      )
    White  = start('255;255;255')
    Green  = start('0;255;0'    )
    Purple = start('255;0;255'  )
    Yellow = start('255;255;0'  )
    Orange = start('255;165;0'  )


class Terminal:
    @staticmethod
    def Clear() -> None:
        return os.system("cls" if os.name == 'nt' else "clear")

    @staticmethod
    def Exit() -> None:
        exit()
    
    @staticmethod
    def Console(ip: str, msg: str, color: str) -> None:
        main = f' [{Col.Green}{ip}{Col.White}] -> '
        print(
            f"{main}{getattr(Col, color)}{msg}{Col.White}"
        )



Terminal.Clear()
start = time.time()


try:
    response = requests.get('https://github.com')
    if response.status_code == 200:
        Terminal.Console('Ping', 'Connect to github.com successful', 'Orange')
    else:
        Terminal.Console('Ping', f'Error: HTTP status code {response.status_code}', 'Red')
        Terminal.Exit()
except Exception as e:
    Terminal.Console('Ping', e, 'Red')
    Terminal.Exit()


try:
    with open('.github/.version', 'r') as file:
        __version__ = file.read()
        
except FileNotFoundError:
    Terminal.Console('GitHub', 'File .version not found', 'Red')
    Terminal.Exit()

except Exception as e:
    Terminal.Console('GitHub', f'Error reading .version file: {e}', 'Red')
    Terminal.Exit()


try:
    run(['git', 'add', '.'], stdout=DEVNULL, stderr=DEVNULL)
    Terminal.Console('GitHub', 'git add .', 'Blue')

    run(['git', 'commit', '-m', __version__], stdout=DEVNULL, stderr=DEVNULL)
    Terminal.Console('GitHub', f'git commit -m "{__version__}"', 'Blue')

    run(['git', 'push', 'origin', 'main'], stdout=DEVNULL, stderr=DEVNULL)
    Terminal.Console('GitHub', 'git push origin main', 'Blue')

    end = time.time()
    elapsed_time = end - start
    Terminal.Console('Timer', f'Elapsed time for push: {elapsed_time:.2f} seconds', 'Yellow')

except FileNotFoundError:
    Terminal.Console('GitHub', 'Git command not found', 'Red')
    Terminal.Exit()

except Exception as e:
    Terminal.Console('GitHub', f'Error executing Git command: {e}', 'Red')
    Terminal.Exit()