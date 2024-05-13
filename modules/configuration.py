




# Màu sắc 
RESET_COLOR = "\033[38;2;255;255;255m"
HIGHLIGHT_COLOR = "\033[38;2;255;255;0m"


# Frames cho hoạt ảnh
FRAMES = [
    f"\r {RESET_COLOR}[{HIGHLIGHT_COLOR}{' ' * i}-->{' ' * (5 - i)}{RESET_COLOR}]"
    for i in range(6)
] + [
    f"\r {RESET_COLOR}[{HIGHLIGHT_COLOR}{' ' * i}<--{' ' * (5 - i)}{RESET_COLOR}]"
    for i in range(5, -1, -1)
]
