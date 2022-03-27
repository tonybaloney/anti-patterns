def try_in_loop():
    items = {
        'a': 1
    }
    for _ in range(100_000):
        try:
            _ = items['a']
        except Exception:
            pass

def try_outside_loop():
    items = {
        'a': 1
    }
    try:
        for _ in range(100_000):
            _ = items['a']
    except Exception:
        pass


__benchmarks__ = [
    (try_in_loop, try_outside_loop, "Refactoring Try..except outside a loop"),
]