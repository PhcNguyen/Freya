from modules.ui.utils import Colors, ui




def home() -> None:
    color = Colors.dynamicMIX([Colors.White, Colors.Purple])
    ui(color, 'home')


def menu() -> None:
    color = Colors.dynamicMIX([Colors.White, Colors.Orange])
    ui(color, 'menu')