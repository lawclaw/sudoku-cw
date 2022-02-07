class TextColors:      # https://www.delftstack.com/howto/python/python-print-colored-text/
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


def paint_print(color, input_str, endl: None):
    if endl is None:
        endl = "\n"
    if color == "g":
        __paint_print_green(input_str, endl)
    elif color == "y":
        __paint_print_yellow(input_str, endl)
    elif color == "r":
        __paint_print_red(input_str, endl)


def __paint_print_green(input_str, endl: None):
    print(TextColors.OK + input_str + TextColors.RESET, end=endl)


def __paint_print_yellow(input_str, endl: None):
    print(TextColors.WARNING + input_str + TextColors.RESET, end=endl)


def __paint_print_red(input_str, endl: None):
    print(TextColors.FAIL + input_str + TextColors.RESET, end=endl)

