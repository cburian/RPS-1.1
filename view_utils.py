
def prt_delimiter(length, border: str = '-'):
    """Applies border to message - for important messages

    todo: make this into a decorator
    """
    print(border * length)


def border_decorator(func):
    """
    decorator to beautify a menu
    prints before and after the menu
    """
    def to_decorate(*args, **kwargs):
        print('-' * 20)
        func(*args, **kwargs)
        print('-' * 20)
    return to_decorate
