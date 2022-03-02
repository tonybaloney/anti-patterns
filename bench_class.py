from collections import namedtuple
from dataclasses import dataclass


def attributes_in_class():
    class Pet:
        legs: int
        noise: str

        def __init__(self, legs, noise) -> None:
            self.legs = legs
            self.noise = noise
        
        def __repr__(self):
            return f"<Pet legs={self.legs} noise='{self.noise}'>"
    
    for _ in range(1000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_dataclass():
    @dataclass
    class Pet:
        legs: int
        noise: str
    
    for _ in range(1000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_namedtuple():
    Pet = namedtuple("Pet", "legs noise")
    for _ in range(1000):
        dog = Pet(4, "woof")
        str(dog)

def attributes_in_dict():
    for _ in range(1000):
        dog = {"legs": 4, "noise": "woof"}
        str(dog)

__benchmarks__ = [ 
    (attributes_in_dataclass, attributes_in_class, "Class instead of dataclass"),
    (attributes_in_dataclass, attributes_in_namedtuple, "Namedtuple instead of dataclass"),
    (attributes_in_namedtuple, attributes_in_class, "class instead of namedtuple"),
    (attributes_in_class, attributes_in_dict, "dict instead of class"),
]