import shutil


class MakeColors:
    terminal_size = shutil.get_terminal_size()

    @staticmethod
    def start_color(color: str) -> str:
        return f"\033[38;2;{color}m"

    @staticmethod
    def make_transition(color: str, text: str) -> str:
        return f"\033[38;2;{color}m{text}\033[38;2;255;255;255m"

    @staticmethod
    def remove_ansi(color: str) -> str:
        return color.replace('\033[38;2;', '').replace('m', '').replace('50m', '').replace('\x1b[38', '')

    @staticmethod
    def count_leading_spaces(text: str) -> int:
        return len(text) - len(text.lstrip())

    @staticmethod
    def reverse_list(colors: list) -> list:
        return list(reversed(colors))

    @staticmethod
    def mix_colors(color1: str, color2: str, reverse: bool = True) -> list:
        color1, color2 = MakeColors.remove_ansi(color=color1), MakeColors.remove_ansi(color=color2)
        fade1 = MakeColors.static_mix([color1, color2], start=False)
        fade2 = MakeColors.static_mix([fade1, color2], start=False)
        fade3 = MakeColors.static_mix([fade1, color1], start=False)
        fade4 = MakeColors.static_mix([fade2, color2], start=False)
        fade5 = MakeColors.static_mix([fade1, fade3], start=False)
        fade6 = MakeColors.static_mix([fade3, color1], start=False)
        fade7 = MakeColors.static_mix([fade1, fade2], start=False)
        mixed = [color1, fade6, fade3, fade5, fade1, fade7, fade2, fade4, color2]
        return MakeColors.reverse_list(colors=mixed) if reverse else mixed

    @staticmethod
    def calculate_spaces(text: str) -> int:
        try:
            columns = MakeColors.terminal_size.columns
        except OSError:
            return 0
        max_text_length = max((len(line) for line in text.splitlines() if line.strip()), default=0)
        return (columns - max_text_length) // 2

    @staticmethod
    def static_mix(colors: list, start: bool = True) -> str:
        rgb = [list(map(int, MakeColors.remove_ansi(color).split(';'))) for color in colors]
        average_rgb = [round(sum(color[i] for color in rgb) / len(rgb)) for i in range(3)]
        rgb_string = ';'.join(map(str, average_rgb))
        return MakeColors.start_color(rgb_string) if start else rgb_string

    @staticmethod
    def dynamic_mix(colors: list) -> list:
        mixed_colors = [MakeColors.mix_colors(color1=colors[i], color2=colors[i + 1], reverse=False) for i in
                        range(len(colors) - 1)]
        flattened_colors = [color for sublist in mixed_colors for color in sublist]
        return MakeColors.reverse_list(colors=flattened_colors)

    @staticmethod
    def center_text_horizontally(text: str, spaces: int = None, icon: str = " ") -> str:
        if spaces is None:
            spaces = MakeColors.calculate_spaces(text=text)
        return "\n".join((icon * spaces) + line for line in text.splitlines())

    @staticmethod
    def diagonal_text(color_list: list, text: str, speed: int = 1, cut: int = 0) -> str:
        color_list = color_list[cut:]
        lines = text.splitlines()
        result = ""
        color_index = 0
        for line in lines:
            characters = list(line)
            for char in characters:
                current_color = color_list[color_index]
                result += " " * MakeColors.count_leading_spaces(char) + MakeColors.make_transition(current_color,
                                                                                                   char.strip())
                if color_index + speed < len(color_list):
                    color_index += speed
                else:
                    color_index = 1
            result += "\n"
        return result.rstrip()

    @staticmethod
    def add_padding(banner: str) -> str:
        banner_lines = banner.splitlines()
        max_length = max(len(line) for line in banner_lines)
        padded_banner = [line.ljust(max_length) for line in banner_lines]
        return '\n'.join(padded_banner)


class Colors:
    red = MakeColors.start_color('255;0;0')
    blue = MakeColors.start_color('28;121;255')
    cyan = MakeColors.start_color('0;255;255')
    pink = MakeColors.start_color('255;192;203')
    black = MakeColors.start_color('0;0;0')
    white = MakeColors.start_color('255;255;255')
    green = MakeColors.start_color('0;255;0')
    purple = MakeColors.start_color('255;0;255')
    yellow = MakeColors.start_color('255;255;0')
    orange = MakeColors.start_color('255;165;0')
