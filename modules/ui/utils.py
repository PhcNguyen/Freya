import json

from modules.settings import UI
from modules.core.color import MakeColors


def ui(
    colors: list,
    banner_key: str, 
) -> None:
    with open(UI, 'r', encoding='utf-8') as file:
        banners = json.load(file)
    banners = MakeColors.add_padding("\n".join(banners[banner_key]))
    print(
        MakeColors.diagonal_text(
            colors, 
            MakeColors.center_text_horizontally(banners)
        )
    )