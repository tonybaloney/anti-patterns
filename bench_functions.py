def func_with_kwargs(**kwargs):
    return kwargs['a'] + kwargs['b'] + kwargs['c']

def func_with_named_args(a, b, c):
    return a + b + c

def keyword_call():
    func_with_kwargs(a=1, b=2, c=3)


def positional_call():
    func_with_named_args(a=1, b=2, c=3)



def add(x, y):
    return x + y

def use_tiny_func():
    x = 1
    for n in range(100_000):
        add(x, n)
        add(n, x)


def inline_tiny_func():
    x = 1
    for n in range(100_000):
        x + n
        n + x



__benchmarks__ = [ 
    (keyword_call, positional_call, "**Kwargs for known keyword args"),
    (use_tiny_func, inline_tiny_func, "Tiny Functions"),
    ]