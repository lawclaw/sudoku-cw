class TextColors:  # https://stackoverflow.com/a/54955094
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def paint_string(input_str, color):
    if color == 'BLACK':
        return f"{TextColors.BLACK}{input_str}{TextColors.RESET}"
    elif color == 'RED':
        return f"{TextColors.RED}{input_str}{TextColors.RESET}"
    elif color == 'GREEN':
        return f"{TextColors.GREEN}{input_str}{TextColors.RESET}"
    elif color == 'YELLOW':
        return f"{TextColors.YELLOW}{input_str}{TextColors.RESET}"
    elif color == 'BLUE':
        return f"{TextColors.BLUE}{input_str}{TextColors.RESET}"
    elif color == 'MAGENTA':
        return f"{TextColors.MAGENTA}{input_str}{TextColors.RESET}"
    elif color == 'CYAN':
        return f"{TextColors.CYAN}{input_str}{TextColors.RESET}"
    elif color == 'WHITE':
        return f"{TextColors.WHITE}{input_str}{TextColors.RESET}"
