from os.path import exists
import os

def dotted_import():
    for _ in range(100_000):
        return os.path.exists('/')

def direct_import():
    for _ in range(100_000):
        return exists('/')

__benchmarks__ = [
    (dotted_import, direct_import, "Importing specific name instead of namespace"),
]