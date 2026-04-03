def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)

    counted.call_count = 0
    return counted


def memo(f):
    cache = {}

    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memorized


def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result

    counted.max_count = 0
    counted.open_count = 0
    return counted
