import os
import sys

from modules import ui
from modules.core import Terminal, System, Github

try:
    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command
except ImportError:
    Terminal.Console("DJANGO", "Red",
        "Đã có lỗi không mong muốn xảy ra ! "
        + "Hãy liên hệ với Developers để khắc phục sự cố."
    )
    Terminal.Exit()


def main(noti = ''):
    Terminal.Clear()
    ui.menu()
    if noti:
        Terminal.Console('MAIN', 'Red', noti)
    else: print('\n')
    select = input(" Select: ")
    if select.isdigit():
        option = int(select)
        actions = {
            0: lambda: Terminal.Exit(),
            1: lambda: runserver(),
            3: lambda: Github()
        }
        if option in actions:
            actions[option]()
        else:
            main('Lựa chọn không hợp lệ!')
    else:
        main('Vui lòng nhập số!')



def runserver():
    runserver.default_addr = System.local_ip()
    runserver.default_port = 8080
    execute_from_command_line(sys.argv + ["runserver"])


if __name__ == '__main__':
    Terminal.Clear()
    ui.home()
    main()