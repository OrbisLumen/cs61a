class Tree:
    """A tree is a label and a list of branches."""

    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return "Tree({0}{1})".format(repr(self.label), branch_str)

    def __str__(self):
        return "\n".join(self.indented())

    def indented(self):
        """each level adds one space to the subtree lines"""
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append(" " + line)
        return [str(self.label)] + lines

    # when reaching a leaf, the code skips the double 'for' loop
    # when processing a node with leaf, the code adds one ' ' to every child

    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    """A Fibonacci tree."""
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


def leaves(t):
    """Return a list of leaf labels in Tree T."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.banches:
            all_leaves.extend(leaves(b))
        return all_leaves


def height(t):
    """Return the number of transitions in the longest path in T."""
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])


def prune(t, n):
    """Prune all sub_trees whose label is n."""

    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)
