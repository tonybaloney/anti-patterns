from typing import Sequence


def sequence_match_logical():
    """ Test matching the first element of a sequence is a frog. """
    seq = ["🐸", "🐛", "🦋", "🪲"]
    frogs = 0
    for _ in range(100_000):
        if isinstance(seq, Sequence) and len(seq) > 0 and seq[0] == "🐸": 
            frogs += 1
    
    assert frogs == 100_000

def sequence_match_statement():
    """ Test matching the first element of a sequence is a frog. """
    seq = ["🐸", "🐛", "🦋", "🪲"]
    frogs = 0
    for _ in range(100_000):
        match seq:
            case ["🐸", *_]: frogs += 1
    
    assert frogs == 100_000

def negative_sequence_match_logical():
    """ Test matching the first element of a sequence is a frog. """
    seq = ["🐛", "🦋", "🪲"]
    frogs = 0
    for _ in range(100_000):
        if isinstance(seq, Sequence) and len(seq) > 0 and seq[0] == "🐸": 
            frogs += 1
    
    assert frogs == 0

def negative_sequence_match_statement():
    """ Test matching the first element of a sequence is a frog. """
    seq = ["🐛", "🦋", "🪲"]
    frogs = 0
    for _ in range(100_000):
        match seq:
            case ["🐸", *_]: frogs += 1
    
    assert frogs == 0

__benchmarks__ = [
    (sequence_match_logical, sequence_match_statement, "Match statements"),
    (negative_sequence_match_logical, negative_sequence_match_statement, "Match statements (negative)")
]