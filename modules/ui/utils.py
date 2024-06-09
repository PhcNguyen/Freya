import json

from modules.settings import UI
from modules.core.utils import Colors


def ui(
    colors: str, 
    banner_key: str, 
) -> None:
    with open(UI, 'r', encoding='utf-8') as file:
        banners = json.load(file)
    print(
        Colors.diagonal(
            colors, 
            Colors.xcenter(Colors.add("\n".join(banners[banner_key])))
        )
    )