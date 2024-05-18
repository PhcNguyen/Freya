import os
import shutil
from pathlib import Path

from .colors import Colors as Col


FRAMES = [
    f"\r {Col.White}[{Col.Yellow}{' ' * i}-->{' ' * (5 - i)}{Col.White}]"
    for i in range(6)
] + [
    f"\r {Col.White}[{Col.Yellow}{' ' * i}<--{' ' * (5 - i)}{Col.White}]"
    for i in range(5, -1, -1)
]


def remove_pycache(directory):
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
