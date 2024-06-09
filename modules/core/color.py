import os
import shutil


class _MakeColors:
    size = shutil.get_terminal_size()

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
        fade1 = Colors.staticMIX([col1, col2], _start=False)      
        fade2 = Colors.staticMIX([fade1, col2], _start=False)
        fade3 = Colors.staticMIX([fade1, col1], _start=False)
        fade4 = Colors.staticMIX([fade2, col2], _start=False)
        fade5 = Colors.staticMIX([fade1, fade3], _start=False)    
        fade6 = Colors.staticMIX([fade3, col1], _start=False)
        fade7 = Colors.staticMIX([fade1, fade2], _start=False)
        mixed = [col1, fade6, fade3, fade5, fade1, fade7, fade2, fade4, col2]
        return _MakeColors._reverse(colors=mixed) if _reverse else mixed
    

class Colors:
    @staticmethod
    def start(color: str) -> str: 
        return f"\033[38;2;{color}m"
    
    @staticmethod
    def _xspaces(text: str):
        try:
            col = _MakeColors.size.columns
        except OSError:
            return 0
        ntextl = max((len(v) for v in text.splitlines() if v.strip()), default=0)
        return (col - ntextl) // 2
    
    def staticMIX(colors: list, _start: bool = True) -> str:
        rgb = [list(map(int, _MakeColors._rmansi(col).split(';'))) for col in colors]
        average_rgb = [round(sum(color[i] for color in rgb) / len(rgb)) for i in range(3)]
        rgb_string = ';'.join(map(str, average_rgb))
        return _MakeColors._start(rgb_string) if _start else rgb_string

    def dynamicMIX(colors: list):
        mixed_colors = [_MakeColors._mixcolors(col1=colors[i], col2=colors[i+1], _reverse=False) for i in range(len(colors)-1)]
        flattened_colors = [col for sublist in mixed_colors for col in sublist]
        return _MakeColors._reverse(colors=flattened_colors)
    
    def xcenter(text: str, spaces: int = None, icon: str = " "):
        if spaces is None:
            spaces = Colors._xspaces(text=text)
        return "\n".join((icon * spaces) + text for text in text.splitlines())
    
    def diagonal(color: list, text: str, speed: int = 1, cut: int = 0) -> str:
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
    
    def add(banner):
        mbanner = banner.splitlines()
        mlength = max(len(line) for line in mbanner)
        fbanner = [line.ljust(mlength) for line in mbanner]
        return '\n'.join(fbanner)
    
    
    Red = start.__func__('255;0;0')
    Blue = start.__func__('28;121;255')
    Cyan = start.__func__('0;255;255')
    Pink = start.__func__('255,192,203')
    Black = start.__func__('0;0;0')
    White = start.__func__('255;255;255')
    Green = start.__func__('0;255;0')
    Purple = start.__func__('255;0;255')
    Yellow = start.__func__('255;255;0')
    Orange = start.__func__('255;165;0')