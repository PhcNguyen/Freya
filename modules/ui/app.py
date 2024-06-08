from modules.core.utils import Colors 
from modules.ui.utils import Color, load_ui


def home() -> None:
    color = Color.DynamicMIX([Colors.White, Colors.Purple])
    load_ui(color, 'home')


def menu() -> None:
    color = Color.DynamicMIX([Colors.White, Colors.Orange])
    load_ui(color, 'menu')

