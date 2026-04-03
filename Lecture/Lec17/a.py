def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
    else:
        yield "Blast off"


def prefixes(s):
    """
    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s


def substrings(s):
    """
    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])


def count_partitions(n, m):
    """Count partitions
    >>> count_partitions(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return exact_match + with_m + without_m


def list_partitions(n, m):
    """
    >>> for p in list_partitions(6,4):print(p)
    [2, 4]
    [1, 1, 4]
    [3, 3]
    [1, 2, 3]
    [1, 1, 1, 3]
    [2, 2, 2]
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 1, 1, 1]
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partitions(n - m, m)]
        without_m = list_partitions(n, m - 1)
        return exact_match + with_m + without_m


def addition_partitions(n, m):

    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + " + " + str(m) for p in addition_partitions(n - m, m)]
        without_m = addition_partitions(n, m - 1)
        return exact_match + with_m + without_m


def yield_addition_partitions(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in yield_addition_partitions(n - m, m):
            yield p + " + " + str(m)
        yield from yield_addition_partitions(n, m - 1)
