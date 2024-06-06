
from typing import Union


class Colors:
    @staticmethod
    def start(color: str) -> str:
        return f"\033[38;2;{color}m"
    
    @classmethod
    def update_color(cls, color_name: str, new_color: str):
        setattr(cls, color_name, cls.start.__func__(new_color))
    
    Red    = start.__func__('255;0;0')
    Blue   = start.__func__('28;121;255')
    Cyan   = start.__func__('0;255;255')
    Pink   = start.__func__('255,192,203')
    Black  = start.__func__('0;0;0')
    White  = start.__func__('255;255;255')
    Green  = start.__func__('0;255;0')
    Purple = start.__func__('255;0;255')
    Yellow = start.__func__('255;255;0')
    Orange = start.__func__('255;165;0')


FRAMES = [
    f"\r {Colors.White}[{Colors.Yellow}{' ' * i}-->{' ' * (5 - i)}{Colors.White}]"
    for i in range(6)
] + [
    f"\r {Colors.White}[{Colors.Yellow}{' ' * i}<--{' ' * (5 - i)}{Colors.White}]"
    for i in range(5, -1, -1)
]

MESSAGE: str = ( Colors.White
    + " ["
    + Colors.Green
    + "{}"
    + Colors.White
    + "] --> "
    + "{}{}" 
    + Colors.White
)