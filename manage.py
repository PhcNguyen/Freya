#!/usr/bin/env python
import os
import sys

from modules import ui
from modules.core import Terminal, System

try:
    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command
    Terminal.Console('DJANGO', 'Green', 'Django setup successfully.')
except ImportError:
    Terminal.Console("DJANGO", "Red",
        "Đã có lỗi không mong muốn xảy ra! "
        + "Hãy liên hệ với Developers để khắc phục sự cố."
    )
    Terminal.Exit()


def main():
    Terminal.Clear()
    ui.home()
    Terminal.Console('SERVER', 'Green', 'Đang khởi tạo server.')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freya.settings")

    try:
        Command.default_addr = System.local_ip()
        Command.default_port = "8080"

        Terminal.Console('SERVER', 'Green', f'Server IP: {Command.default_addr}')
        Terminal.Console('SERVER', 'Green', f'Server Port: {Command.default_port}')

        execute_from_command_line(
            [sys.argv[0], "runserver"]
        )
    except Exception as e:
        Terminal.Console("SERVER", "Red", f"Không thể khởi động server: {e}")
        Terminal.Exit()


if __name__ == '__main__':
    main()