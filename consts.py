from enum import Enum

board_size = 21


class Plant(Enum):
    Wattle = 0
    GumTree = 1

class Animal(Enum):
    Kangaroo = 0
    Emu = 1
    Wombat = 2
    Platypus = 3

animal_array = [Animal.Emu, Animal.Emu,
                Animal.Emu, Animal.Emu,
                Animal.Wombat, Animal.Wombat,
                Animal.Platypus, Animal.Platypus]

class Color(Enum):
    Yellow = 0
    Green = 1