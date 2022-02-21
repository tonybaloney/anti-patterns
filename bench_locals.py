
def slice_copy_to_fast():
    x = list(range(100000))
    y = list(range(100000))

    for n in range(100000):
        i = x[n]
        j = y[n]
        i + j
        i + j
        i + j
        i + j
        i + j

def slice_as_local():
    x = list(range(100000))
    y = list(range(100000))

    for n in range(100000):
        x[n] + y[n]
        x[n] + y[n]
        x[n] + y[n]
        x[n] + y[n]
        x[n] + y[n]

x = 34567890
y = 12345673

def copy_name_to_fast():
    i = x
    j = y

    for _ in range(100000):
        i + j
        i + j
        i + j
        i + j
        i + j

def as_local():
    for _ in range(100000):
        x + y
        x + y
        x + y
        x + y
        x + y


d = {
    "x": 1234,
    "y": 5678,
}

def copy_dict_key_to_fast():
    i = d["x"]
    j = d["y"]

    for _ in range(100000):
        i + j
        i + j
        i + j
        i + j
        i + j

def dont_copy_dict_key_to_fast():
    for _ in range(100000):
        d["x"] + d["y"]
        d["x"] + d["y"]
        d["x"] + d["y"]
        d["x"] + d["y"]
        d["x"] + d["y"]


class Foo:
    x = 1
    y = 2

foo = Foo()

def copy_attr_to_fast():
    i = foo.x
    j = foo.y

    for _ in range(100000):
        i + j
        i + j
        i + j
        i + j
        i + j

def dont_copy_attr_to_fast():
    for _ in range(100000):
        foo.x + foo.y
        foo.x + foo.y
        foo.x + foo.y
        foo.x + foo.y
        foo.x + foo.y


__benchmarks__ = [ 
    (slice_as_local, slice_copy_to_fast, "Copy slice to Local"),
    (as_local, copy_name_to_fast, "Copy name to Local"),
    (dont_copy_dict_key_to_fast, copy_dict_key_to_fast, "Copy dict item to Local"),
    (dont_copy_attr_to_fast, copy_attr_to_fast, "Copy class attr to Local"),
    ]