# The first abstraction: Tree Structure


def tree(label, branches=[]):
    """a function to build tree"""
    for branch in branches:
        # if branches=[], the loop will pass
        assert is_tree(branch)
    return [label] + list(branches)  # use list to build outer list


def label(tree):
    """return the label of one tree"""
    return tree[0]


def branches(tree):
    """return the branches of one tree"""
    return tree[1:]


def is_tree(tree):
    """judge whether it is a tree"""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):  # judge every branches recursively
            return False
    return True


def is_leaf(tree):
    """judge whether it is a leaf"""
    return not branches(tree)


def fib_tree(n):
    """build Fibonacci trees recursively

    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    """
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])


# The second abstraction: Tree processing funcs


def count_leaves(t):
    """Count the leaves of a tree.

    >>> count_leaves(fib_tree(10))
    89
    """
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)


def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])


def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)


def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


def print_tree(t, indent=0):
    print(" " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def print_sums(t, so_far):
    """
    Print the sum of labels from the root to each leaf of tree t.

    so_far is the sum of labels along the path from the root to the
    parent of the current node.
    """
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


def sum_paths(t):
    """Return a list of sums from the root to each leaf."""

    if is_leaf(t):
        return [label(t)]

    result = []

    for b in branches(t):
        for s in sum_paths(b):
            result.append(label(t) + s)

    return result


def count_paths(t, total):
    """
    Return the number of paths from the root to any node in tree t
    for which the labels along the path sum to total

    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0

    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])
