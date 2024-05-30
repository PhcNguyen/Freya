#!/usr/bin/env python
import os
import sys
from modules.core import Terminal


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freya.settings')
    try:
        from django.core.management import execute_from_command_line
    except:
        Terminal.Console("DJANGO", "Red",
            "Đã có lỗi không mong muốn xảy ra ! Hãy liên hệ với Developers."
        )
        return
    execute_from_command_line(sys.argv)


if __name__ == '__main__':  
    main()
