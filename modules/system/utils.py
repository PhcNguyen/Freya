import os
import shutil


white = "\033[38;2;255;255;255m"
yellow = "\033[38;2;255;255;0m"
FRAMES = [
    f"\r {white}[{yellow}{' ' * i}-->{' ' * (5 - i)}{white}]"
    for i in range(6)
] + [
    f"\r {white}[{yellow}{' ' * i}<--{' ' * (5 - i)}{white}]"
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
