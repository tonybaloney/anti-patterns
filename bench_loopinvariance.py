
def before():
    x = (1, 2, 3, 4)
    i = 6

    for j in range(100_000):
        # x is never changed in this loop scope,
        # so this expression is invariant
        len(x) * i + j


def after():
    x = (1, 2, 3, 4)
    i = 6
    x_i = len(x) * i
    for j in range(100_000):
        x_i + j

__benchmarks__ = [
    (before, after, "Loop invariant Code Motion"),
]