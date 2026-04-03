from rational import rational, numer, denom


def mul_rational(x, y):
    """Add rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def add_rational(x, y):
    """Multiply rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def equal_rational(x, y):
    """Return whether rational numbers x and y are equal"""
    return numer(x) * denom(y) == numer(y) * denom(x)


def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))
