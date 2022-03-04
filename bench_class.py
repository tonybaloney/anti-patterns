from collections import namedtuple
from dataclasses import dataclass
import typing


def attributes_in_class():
    class Pet:
        legs: int
        noise: str

        def __init__(self, legs, noise) -> None:
            self.legs = legs
            self.noise = noise
        
        def __repr__(self):
            return f"<Pet legs={self.legs} noise='{self.noise}'>"
    
    for _ in range(100000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_class_with_slots():
    class Pet:
        legs: int
        noise: str
        __slots__ = 'legs', 'noise'

        def __init__(self, legs, noise) -> None:
            self.legs = legs
            self.noise = noise
        
        def __repr__(self):
            return f"<Pet legs={self.legs} noise='{self.noise}'>"
    
    for _ in range(100000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_dataclass():
    @dataclass
    class Pet:
        legs: int
        noise: str
    
    for _ in range(100000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_dataclass_with_slots():
    @dataclass(slots=True)
    class Pet:
        legs: int
        noise: str
    
    for _ in range(100000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_namedtuple():
    Pet = namedtuple("Pet", "legs noise")
    for _ in range(100000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_namedtuple_type():
    class Pet(typing.NamedTuple):
        legs: int
        noise: str

    for _ in range(100000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_dict():
    for _ in range(100000):
        dog = {"legs": 4, "noise": "woof"}
        str(dog)

__benchmarks__ = [ 
    (attributes_in_dataclass, attributes_in_class, "Class instead of dataclass"),
    (attributes_in_dataclass, attributes_in_dataclass_with_slots, "dataclass with slots"),
    (attributes_in_dataclass, attributes_in_namedtuple, "Namedtuple instead of dataclass"),
    (attributes_in_namedtuple, attributes_in_class, "class instead of namedtuple"),
    (attributes_in_namedtuple, attributes_in_namedtuple_type, "namedtuple class instead of namedtuple"),
    (attributes_in_class, attributes_in_dict, "dict instead of class"),
    (attributes_in_class, attributes_in_class_with_slots, "class with slots"),
]
