#!/usr/bin/env python
import os
import sys

from modules.core import System
from modules.core.utils import ERROR_MESSAGE



try:
    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command
    System.console('DJANGO', 'Green', 'Django setup successfully.')
except ImportError:
    System.console("DJANGO", "Red", ERROR_MESSAGE)
    System.exit()


def main():
    System.clear()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freya.settings")

    try:
        Command.default_addr = System.localIP()
        Command.default_port = "8080"
        execute_from_command_line(
            [sys.argv[0], "runserver"]
        )
    except Exception as error:
        System.console("SERVER", "Red", str(error))
        System.exit()



if __name__ == '__main__':
    main()
