import json
from modules.settings import UI
from modules.core.utils import Colors as Col
from os import name as _name, system as _system, get_terminal_size as _terminal_size


class _MakeColors:
    @staticmethod
    def _makeansi(col: str, text: str) -> str:
        return f"\033[38;2;{col}m{text}\033[38;2;255;255;255m"
    
    @staticmethod
    def _rmansi(col: str) -> str:
        return col.replace('\033[38;2;', '').replace('m','').replace('50m', '').replace('\x1b[38', '')
    
    @staticmethod
    def _getspaces(text: str) -> int:
        return len(text) - len(text.lstrip())
    
    @staticmethod
    def _reverse(colors: list) -> list:
        _colors = list(colors)
        for col in reversed(_colors):
            colors.append(col)
        return colors
    
    @staticmethod
    def _mixcolors(col1: str, col2: str, _reverse: bool = True) -> list:
        col1, col2 = _MakeColors._rmansi(col=col1), _MakeColors._rmansi(col=col2)
        fade1 = Color.StaticMIX([col1, col2], _start=False)      
        fade2 = Color.StaticMIX([fade1, col2], _start=False)
        fade3 = Color.StaticMIX([fade1, col1], _start=False)
        fade4 = Color.StaticMIX([fade2, col2], _start=False)
        fade5 = Color.StaticMIX([fade1, fade3], _start=False)    
        fade6 = Color.StaticMIX([fade3, col1], _start=False)
        fade7 = Color.StaticMIX([fade1, fade2], _start=False)
        mixed = [col1, fade6, fade3, fade5, fade1, fade7, fade2, fade4, col2]
        return _MakeColors._reverse(colors=mixed) if _reverse else mixed


class Color:
    @staticmethod
    def _xspaces(text: str):
        try:
            col = _terminal_size().columns
        except OSError:
            return 0
        ntextl = max((len(v) for v in text.splitlines() if v.strip()), default=0)
        return (col - ntextl) // 2

    def DynamicMIX(colors: list):
        mixed_colors = [_MakeColors._mixcolors(col1=colors[i], col2=colors[i+1], _reverse=False) for i in range(len(colors)-1)]
        flattened_colors = [col for sublist in mixed_colors for col in sublist]
        return _MakeColors._reverse(colors=flattened_colors)
    
    def StaticMIX(colors: list, _start: bool = True) -> str:
        rgb = [list(map(int, _MakeColors._rmansi(col).split(';'))) for col in colors]
        average_rgb = [round(sum(color[i] for color in rgb) / len(rgb)) for i in range(3)]
        rgb_string = ';'.join(map(str, average_rgb))
        return _MakeColors._start(rgb_string) if _start else rgb_string
    
    def XCenter(text: str, spaces: int = None, icon: str = " "):
        if spaces is None:
            spaces = Color._xspaces(text=text)
        return "\n".join((icon * spaces) + text for text in text.splitlines())
    
    def Diagonal(color: list, text: str, speed: int = 1, cut: int = 0) -> str:
        color = color[cut:]
        lines = text.splitlines()
        result = ""
        color_n = 0
        for lin in lines:
            carac = list(lin)
            for car in carac:
                colorR = color[color_n]
                result += " " * _MakeColors._getspaces(car) + _MakeColors._makeansi(colorR, car.strip())
                if color_n + speed < len(color):
                    color_n += speed
                else:
                    color_n = 1
            result += "\n"
        return result.rstrip()
    
    def Add(banner):
        mbanner = banner.splitlines()
        mlength = max(len(line) for line in mbanner)
        fbanner = [line.ljust(mlength) for line in mbanner]
        return '\n'.join(fbanner)


def load_ui(
    colors: str, 
    banner_key: str, 
) -> None:
    with open(UI, 'r', encoding='utf-8') as file:
        banners = json.load(file)
    print(
        Color.Diagonal(
            colors, 
            Color.XCenter(Color.Add("\n".join(banners[banner_key])))
        )
    )