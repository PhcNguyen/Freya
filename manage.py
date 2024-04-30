#!/usr/bin/env python
import os
import sys
from socket import (
    socket,
    AF_INET,
    SOCK_DGRAM
)

def local_ip() -> str:
    try:
        server = socket(AF_INET, SOCK_DGRAM)
        server.connect(("8.8.8.8", 80))
        ip = server.getsockname()[0]
        server.close()
        return ip
    except Exception as e:
        print(f"ERROR: {e}")
        return None


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freya.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "DA CO LOI XAY RA."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':  
    main()
