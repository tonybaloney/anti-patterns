import gc

def _cyclic_references():
    l = []
    t = (l, )
    l.append(t)
    d = {}
    d['t'] = t
    d['d'] = d

def load_gc_at_end():
    t1, t2, t3 = gc.get_threshold()
    gc.set_threshold(10, 10, 10)
    for _ in range(100_000):
        _cyclic_references()
    gc.set_threshold(t1, t2, t3)

def load_with_gc():
    t1, t2, t3 = gc.get_threshold()
    gc.set_threshold(1000, 20, 20)
    for _ in range(100_000):
        _cyclic_references()
    gc.set_threshold(t1, t2, t3)

__benchmarks__ = [
    (load_with_gc, load_gc_at_end, "GC with higher threshold"),
]