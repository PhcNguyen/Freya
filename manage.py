#!/usr/bin/env python
import os
import sys

from modules import ui
from modules.core import System
from modules.settings import ERROR_MESSAGE

try:
    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command
    System.console('DJANGO', 'Green', 'Django setup successfully.')
except ImportError:
    System.console("DJANGO", "Red", ERROR_MESSAGE)
    System.exit()


def main():
    System.clear()
    ui.home()
    System.console('SERVER', 'Green', 'Bắt đầu khởi động server.')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freya.settings")

    try:
        Command.default_addr = System.loaclIP()
        Command.default_port = "8080"

        System.console('SERVER', 'Green', f'IP: {Command.default_addr}')
        System.console('SERVER', 'Green', f'Port: {Command.default_port}')

        execute_from_command_line(
            [sys.argv[0], "runserver"]
        )
    except:
        System.console("SERVER", "Red", ERROR_MESSAGE)
        System.exit()


if __name__ == '__main__':
    main()