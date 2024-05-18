import sys
import os
import time
from typing import NoReturn

from .colors import Colors as Col
from .utils import FRAMES


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
    def Console(title: str, msg: str, color: str) -> bool:
        try:
            msg = str(msg)
            colors = getattr(Col, color)
            lines = f'{Col.White}[{Col.Orange}{title}{Col.White}] --> '
            print(f"{lines}{colors}{msg}{Col.White}")
            return True
        except Exception as error:
            return False
    
    @staticmethod
    def Sleep(times: int) -> None:
        for i in range(times, 0, -1):
            for frame in FRAMES:
                sys.stdout.write(f'{frame}[{Col.Orange}{i:02}{Col.White}]')
                sys.stdout.flush()
                time.sleep(0.125)
        sys.stdout.write('\r')