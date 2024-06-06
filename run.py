from modules import ui
from modules.core import Terminal, Github


def main(noti=''):
    Terminal.Clear()
    ui.menu()
    if noti:
        Terminal.Console('MAIN', 'Red', noti)
    else:
        print('\n')
    select = input(" Select: ")
    if select.isdigit():
        option = int(select)
        actions = {
            0: lambda: Terminal.Exit(),
            3: lambda: Github()
        }
        if option in actions:
            actions[option]()
        else:
            main('Lựa chọn không hợp lệ!')
    else:
        main('Vui lòng nhập số!')


if __name__ == '__main__':
    Terminal.Clear()
    ui.home()
    main()
