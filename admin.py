#!/usr/bin/env python
import os
import sys

from modules.core import System
from modules.core.utils import ERROR_MESSAGE



if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freya.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        System.console("DJANGO", "Red", ERROR_MESSAGE)
        System.exit()
    execute_from_command_line(sys.argv)
