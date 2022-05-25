def filter_list_as_loop():
    result = []
    inputs = range(100_000)
    for i in inputs:
        if i % 2:
            result.append(i)

def filter_list_as_comprehension():
    inputs = range(100_000)
    result = [i for i in inputs if i % 2]

def join_generator_expression():
    words = ['data', 'type', 'is', 'so', 'long', 'now']
    for x in range(100_000):
        ''.join(ele.title() for ele in words)

def join_list_comprehension():
    words = ['data', 'type', 'is', 'so', 'long', 'now']
    for x in range(100_000):
        ''.join([ele.title() for ele in words])

__benchmarks__ = [
    (filter_list_as_loop, filter_list_as_comprehension, "Using a list comprehension to filter another list"),
    (join_generator_expression, join_list_comprehension, "Join list comprehension instead of generator expression"),
]
