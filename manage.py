#!/usr/bin/env python
import os
import sys
from modules import IP_LOCAL

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freya.settings')
    try:
        from django.core.management import execute_from_command_line
        sys.argv.append(f'runserver {IP_LOCAL}:8000')
    except ImportError as exc:
        raise ImportError(
            "Đã có lỗi không mong muốn xảy ra ! Hãy liên hệ với Dev của web."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':  
    main()
