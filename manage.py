#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freya.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Đã có lỗi không mong muốn xảy ra ! Hãy liên hệ với Dev của web."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':  
    main()
