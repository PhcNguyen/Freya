from modules.ui.utils import ui
from modules.core.color import Colors, MakeColors


def home() -> None:
    color = MakeColors.dynamic_mix([Colors.white, Colors.purple])
    ui(color, 'home')


def menu() -> None:
    color = MakeColors.dynamic_mix([Colors.white, Colors.orange])
    ui(color, 'menu')
