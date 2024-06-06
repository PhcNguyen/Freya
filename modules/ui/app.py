from modules.ui.utils import Color, Col, load_ui


def home() -> None:
    color = Color.DynamicMIX([Col.White, Col.Purple])
    load_ui(color, 'home')
    input()


def menu() -> None:
    color = Color.DynamicMIX([Col.White, Col.Orange])
    load_ui(color, 'menu')

