#!/usr/bin/env python
import os
import sys

from modules import ui
from modules.core import Terminal, System
from modules.settings import ERROR_MESSAGE

try:
    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command
    Terminal.Console('DJANGO', 'Green', 'Django setup successfully.')
except ImportError:
    Terminal.Console("DJANGO", "Red", ERROR_MESSAGE)
    Terminal.Exit()


def main():
    Terminal.Clear()
    ui.home()
    Terminal.Console('SERVER', 'Green', 'Bắt đầu khởi động server.')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freya.settings")

    try:
        Command.default_addr = System.local_ip()
        Command.default_port = "8080"

        Terminal.Console('SERVER', 'Green', f'IP: {Command.default_addr}')
        Terminal.Console('SERVER', 'Green', f'Port: {Command.default_port}')

        execute_from_command_line(
            [sys.argv[0], "runserver"]
        )
    except:
        Terminal.Console("SERVER", "Red", ERROR_MESSAGE)
        Terminal.Exit()


if __name__ == '__main__':
    main()