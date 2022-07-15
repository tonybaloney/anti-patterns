from typing import Mapping, Sequence


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

def literal_match_logical():
    """ Test matching of literal values"""
    seq = ["🐊", "🐛", "🐈", "🦋", "🪲", "🐳"]
    butterflies = 0
    caterpillars = 0
    beetles = 0
    for _ in range(100_000):
        for x in seq:
            if x == "🦋": 
                butterflies += 1
            elif x == "🐛":
                caterpillars += 1
            elif x == "🪲":
                beetles += 1
    
    assert butterflies == 100_000
    assert beetles == 100_000
    assert caterpillars == 100_000

def literal_match_statement():
    """ Test matching of literal values """
    seq = ["🐊", "🐛", "🐈", "🦋", "🪲", "🐳"]
    butterflies = 0
    caterpillars = 0
    beetles = 0
    for _ in range(100_000):
        for x in seq:
            match x:
                case "🦋": butterflies += 1
                case "🐛": caterpillars += 1
                case "🪲": beetles += 1
    
    assert butterflies == 100_000
    assert beetles == 100_000
    assert caterpillars == 100_000

def mapping_match_logical():
    """ Test matching of mapping type"""
    boats = [
        {"🐓": 1, },
        {"🦊": 1, "🌽": 1},
        {"🐓": 1, "🌽": 1},
        {"🐓": 1, "🦊": 1},
    ]
    problems = 0
    valid_boats = 0
    for _ in range(100_000):
        for boat in boats:
            if isinstance(boat, Mapping):
                if "🐓" in boat and "🌽" in boat: 
                    problems += 1
                elif "🐓" in boat and "🦊" in boat: 
                    problems += 1
                else:
                    valid_boats += 1
                    
    
    assert valid_boats == 200_000
    assert problems == 200_000

def mapping_match_statement():
    """ Test matching of mapping type"""
    boats = [
        {"🐓": 1, },
        {"🦊": 1, "🌽": 1},
        {"🐓": 1, "🌽": 1},
        {"🐓": 1, "🦊": 1},
    ]
    problems = 0
    valid_boats = 0
    for _ in range(100_000):
        for boat in boats:
            match boat:
                case {"🐓": _, "🌽": _}: problems += 1
                case {"🐓": _, "🦊": _}: problems += 1
                case _: valid_boats += 1
    
    assert valid_boats == 200_000
    assert problems == 200_000

class Driver:
    def __init__(self, name, team, **extra):
        self.name = name
        self.team = team
        self.extra = extra

def bench_class_matching_statement():
    drivers = [
        Driver(name="Max Verstappen", team="Red Bull", ),
        Driver(name="Sergio Perez", team="Red Bull", ),
        Driver(name="Charles Leclerc", team="Ferrari", ),
        Driver(name="Lewis Hamilton", team="Mercedes", ),
    ]

    for _ in range(100_000):
        for driver in drivers:
            match driver:
                case Driver(name="Max Verstappen"): desc = f"Max Verstappen, the current world #1"
                case Driver(name=name, team="Ferrari"): desc = f"{name}, a Ferrari driver!! 🐎"
                case Driver(name=name, team=team): desc = f"{name}, a {team} driver."
                case _: desc = "Invalid request"
            # print(desc)


def bench_class_matching_logical():
    drivers = [
        Driver(name="Max Verstappen", team="Red Bull", ),
        Driver(name="Sergio Perez", team="Red Bull", ),
        Driver(name="Charles Leclerc", team="Ferrari", ),
        Driver(name="Lewis Hamilton", team="Mercedes", ),
    ]

    for _ in range(100_000):
        for driver in drivers:
            if not isinstance(driver, Driver):
                desc = "Invalid request"
            elif driver.name == "Max Verstappen":
                desc = f"Max Verstappen, the current world #1"
            elif driver.team == "Ferrari": 
                desc = f"{driver.name}, a Ferrari driver!! 🐎"
            else:
                desc = f"{driver.name}, a {driver.team} driver."
            # print(desc)


__benchmarks__ = [
    (sequence_match_logical, sequence_match_statement, "Match statements (sequence)"),
    (literal_match_logical, literal_match_statement, "Match statements (literal)"),
    (mapping_match_logical, mapping_match_statement, "Match statements (mapping)"),
    (bench_class_matching_logical, bench_class_matching_statement, "Match statements (classes)"),
]