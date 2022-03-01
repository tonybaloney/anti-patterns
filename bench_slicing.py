def bytes_slice():
    """Slice using normal bytes"""
    word = b'A' * 1000
    for i in range(1000):
        n = word[0:i]

def memoryview_slice():
    """Convert to a memoryview first."""
    word = memoryview(b'A' * 1000)
    for i in range(1000):
        n = word[0:i]


__benchmarks__ = [
    (bytes_slice, memoryview_slice, "Slicing with memoryview instead of bytes"),
]
