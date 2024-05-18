from .colors import Colors as Col


FRAMES = [
    f"\r {Col.White}[{Col.Yellow}{' ' * i}-->{' ' * (5 - i)}{Col.White}]"
    for i in range(6)
] + [
    f"\r {Col.White}[{Col.Yellow}{' ' * i}<--{' ' * (5 - i)}{Col.White}]"
    for i in range(5, -1, -1)
]