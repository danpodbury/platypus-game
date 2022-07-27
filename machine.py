from enum import Enum
from typing import List
import random
import consts

class Machine:
    def __init__(self, name: str):
        self.state_table: List[consts.Color] = []
        self.position: int = 11
        self.animal: consts.Animal = consts.Animal.Kangaroo
        self.name: str = name
        self.score:int = 0
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

    def make_decision(self, current_color):
        decision = []

        for i in range(len(self.state_table)):

            # if this column matches the current state we've found our return
            if (self.state_table[i][0] == current_color and self.state_table[i][1] == self.animal):
                decision.append(self.state_table[i][2]) # append matching color
                decision.append(self.state_table[i][3]) # append matching animal

                # append matching direction
                if (self.state_table[i][4] == consts.Plant.GumTree):
                    decision.append("<")
                if (self.state_table[i][4] == consts.Plant.Wattle):
                    decision.append(">") 
                break

        if (decision == []):
            # the only reason decision is empty here is if we've match a green 
            # platypus which doesn't exist in the table, so we append it here
            #decision = [consts.Color.Green, consts.Animal.Platypus, "X"]
            pass
        return decision

    def move_right(self):
        self.position += 1
        if (self.position > consts.board_size - 1):
            self.position = 0

    def move_left(self):
        self.position -= 1
        if (self.position < 0):
            self.position = consts.board_size - 1

    def render_animal(self):
        #print("===>" + str(self.animal))
        return str(self.animal)[len("Animal."):len("Animal.")+1]