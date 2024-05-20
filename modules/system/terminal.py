import sys
import os
import time
from typing import NoReturn

from .utils import FRAMES



class Col:
    @staticmethod
    def start(color: str) -> str:
        return f"\033[38;2;{color}m"
    
    @classmethod
    def update_color(cls, color_name: str, new_color: str):
        setattr(cls, color_name, cls.start.__func__(new_color))
    
    Red = start.__func__('255;0;0')
    Blue = start.__func__('28;121;255')
    Cyan = start.__func__('0;255;255')
    Pink = start.__func__('255,192,203')
    Black = start.__func__('0;0;0')
    White = start.__func__('255;255;255')
    Green = start.__func__('0;255;0')
    Purple = start.__func__('255;0;255')
    Yellow = start.__func__('255;255;0')
    Orange = start.__func__('255;165;0')


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
        white = Col.White
        subject = (
            f'{white}[{Col.Orange}' +
            '{}' + 
            f'{white}]' + 
            ' --> '
        )
        try:
            msg = str(message)
            colors = getattr(Col, color)
            print(f"{subject.format(title)}{colors}{msg}{white}")
            return True
        except Exception as error:
            print(f"{subject.format('Terminal')}{colors}{error}{white}")
            return False
    
    @staticmethod
    def Sleep(times: int) -> None:
        for i in range(times, 0, -1):
            for frame in FRAMES:
                sys.stdout.write(f'{frame}[{Col.Orange}{i:02}{Col.White}]')
                sys.stdout.flush()
                time.sleep(0.125)
        sys.stdout.write('\r')