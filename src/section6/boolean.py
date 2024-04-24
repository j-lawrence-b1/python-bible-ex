#!/usr/bin/env python3

"""T."""

x_val = 0
y_val = 0


def side_effect_x() -> int:
    global x_val
    x_val += 1

    return x_val


def side_effect_y() -> int:
    global y_val
    y_val += 1

    return y_val


def true_type():
    """The true_type function."""

    return type(True)


def false_type():
    """The false_type function."""

    return type(False)


def truthiness(*args) -> bool:
    """The truthiness function."""

    return all(args)


def falsiness(*args) -> bool:
    """The falsiness function."""

    return False if any(args) else True


def and_short_stop() -> bool:
    """The and_short_stop function."""

    global x_val, y_val
    x_val = 0
    y_val = 0
    a_val = 0
    a_val and side_effect_x() and side_effect_y()
    print(f"a_val[{a_val}], x_val[{x_val}], y_val[{y_val}]")

    return True if (a_val + x_val + y_val) == 0 else False


def main():
    """The main thing."""

    return true_type() and false_type() and truthiness(1) and falsiness(0)
