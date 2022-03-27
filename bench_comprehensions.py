def filter_list_as_loop():
    result = []
    inputs = range(100_000)
    for i in inputs:
        if i % 2:
            result.append(i)

def filter_list_as_comprehension():
    inputs = range(100_000)
    result = [i for i in inputs if i % 2]


__benchmarks__ = [
    (filter_list_as_loop, filter_list_as_comprehension, "Using a list comprehension to filter another list"),
]