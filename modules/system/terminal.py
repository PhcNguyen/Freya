import sys
import os
import time

from .colors import Colors as Col
from ..configuration import FRAMES


class Terminal:
    Windows = os.name == 'nt'

    @staticmethod
    def Clear() -> None:
        os.system("cls" if Terminal.Windows else "clear")

    @staticmethod
    def Title(title: str) -> None:
        if Terminal.Windows:
            os.system(f"title {title}")

    @staticmethod
    def Size(x: int, y: int) -> None:
        if Terminal.Windows:
            os.system(f"mode {x}, {y}")

    @staticmethod
    def Reset() -> None:
        os.execv(sys.executable, ['python'] + sys.argv)

    @staticmethod
    def Exit() -> None:
        sys.exit()

    @staticmethod
    def Command(command: str) -> int:
        return os.system(command)

    @staticmethod
    def Console(
        title: str, 
        msg: str, 
        color: str = 'White'
) -> None:
        lines = f' {Col.White}[{Col.Orange}{title}{Col.White}] --> '
        print(f"{lines}{getattr(Col, color)}{str(msg)}{Col.White}")
    
    @staticmethod
    def Delay(times: float) -> None:
        for i in range(times, 0, -1):
            for frame in FRAMES:
                sys.stdout.write(f'{frame}[{Col.Orange}{i:02}{Col.White}]')
                sys.stdout.flush()
                time.sleep(0.125)
        sys.stdout.write('\r')