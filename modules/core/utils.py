import os.path

from modules.core.style import Colors
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = False


VERSION: str = open(
    os.path.join(BASE_DIR, '.github', 'VERSION')
).read().strip()


FRAMES: list[str] = [
    f"\r {Colors.white}[{Colors.yellow}{' ' * i}-->{' ' * (5 - i)}{Colors.white}]" 
    for i in range(6)
    ] + [
    f"\r {Colors.white}[{Colors.yellow}{' ' * i}<--{' ' * (5 - i)}{Colors.white}]" 
    for i in range(5, -1, -1)
]


# * Message *
MESSAGE: str = f"{Colors.white}[{Colors.green}{{}}{Colors.white}] --> {{}}{{}}{Colors.white}"

ERROR_MESSAGE: str = "Đã có lỗi không mong muốn xảy ra."
