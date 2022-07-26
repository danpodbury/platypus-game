from enum import Enum
import random
from typing import List
import consts

class Machine:
    state_table: List[consts.Color] = []
    position: int = 11
    animal: consts.Animal = consts.Animal.Kangaroo
    name: str = ""
    score:int = 0

    def __init__(self, name: str):
        self.name = name
        self.init_random_table()

    def init_random_table(self):
        for i in range(7):
            col = []
            for j in range(5):
                col.append(consts.Color.Yellow if (i%2==0) else consts.Color.Green)
                col.append(consts.animal_array[i])
                col.append(random.choice(list(consts.Color)))
                col.append(random.choice(list(consts.Animal)))
                col.append(random.choice(list(consts.Plant)))

            self.state_table.append(col)

    def print_table(self):
        for j in range(5):
            line = ""
            for i in range(7):
                line += str(self.state_table[i][j].value) + " "
            print(line)
