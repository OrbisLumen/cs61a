from math import gcd


def rational(n, d):
    """Construct a rational number that represents N/D."""
    g = gcd(n, d)

    def select(name):
        if name == "n":
            return n // g
        elif name == "d":
            return d // g

    return select


def numer(x):
    """Return the numerator of rational number X."""
    return x("n")


def denom(x):
    """Return the denominator of rational number X."""
    return x("d")
