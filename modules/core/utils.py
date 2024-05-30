import os.path
import shutil
from typing import Union


WHI = "\033[38;2;255;255;255m"
YEL = "\033[38;2;255;255;0m"
FRAMES = [
    f"\r {WHI}[{YEL}{' ' * i}-->{' ' * (5 - i)}{WHI}]" for i in range(6)
    ] + [
    f"\r {WHI}[{YEL}{' ' * i}<--{' ' * (5 - i)}{WHI}]" for i in range(5, -1, -1)
]


def removePycache(directory) -> None:
    """
    from pathlib import Path
    remove_pycache(Path.cwd())
    """
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                pycache_dir = os.path.join(root, dir_name)
                shutil.rmtree(pycache_dir)
        for file_name in files:
            if file_name.endswith(".pyc") or file_name.endswith(".pyo"):
                pyc_file = os.path.join(root, file_name)
                os.remove(pyc_file)


def localIP() -> Union[str, dict]:
    try:
        from socket import (
            socket,
            AF_INET,
            SOCK_DGRAM
        )
        with socket(AF_INET, SOCK_DGRAM) as dns:
            dns.connect(("8.8.8.8", 80))
        return dns.getsockname()[0]
    except Exception as error:
        return {'error': error}