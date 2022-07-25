from enum import Enum
import random
from typing import List


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

class Machine:
    state_table: List[Color] = []
    position: int = 11
    animal:Animal = Animal.Kangaroo
    name: str = ""
    score:int = 0

    def __init__(self, name: str):
        self.name = name
        self.init_random_table()

    def init_random_table(self):
        for i in range(7):
            col = []
            for j in range(5):
                col.append(Color.Yellow if (i%2==0) else Color.Green)
                col.append(animal_array[i])
                col.append(random.choice(list(Color)))
                col.append(random.choice(list(Animal)))
                col.append(random.choice(list(Plant)))

            self.state_table.append(col)

    def print_table(self):
        for j in range(5):
            line = ""
            for i in range(7):
                line += str(self.state_table[i][j].value) + " "
            print(line)

class Board:
    size: int = 21
    state: List[Color] = []

    def __init__(self):
        self.state = [Color.Yellow] * self.size

    def print_board(self):
        string = ""
        for char in self.state:
            s = "Y" if char == Color.Yellow else "G"
            string += s
        print(string)

if (__name__ == "__main__"):
    print("Welcome to Platypus game")

    b = Board()
    b.print_board()

    p = Machine("bot01")
    p.print_table()
