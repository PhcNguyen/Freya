from modules.core.color import Colors


FRAMES: str = [
    f"\r {Colors.White}[{Colors.Yellow}{' ' * i}-->{' ' * (5 - i)}{Colors.White}]" 
    for i in range(6)
    ] + [
    f"\r {Colors.White}[{Colors.Yellow}{' ' * i}<--{' ' * (5 - i)}{Colors.White}]" 
    for i in range(5, -1, -1)
]

MESSAGE: str = ( Colors.White
    + "["
    + Colors.Green
    + "{}"
    + Colors.White
    + "] --> "
    + "{}{}" 
    + Colors.White
)