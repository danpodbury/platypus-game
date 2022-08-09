from enum import Enum
from typing import List
import random
import consts

class Machine:
    def __init__(self, name: str, table: List[List[str]] = []):
        self.state_table: List[consts.Color] = []
        self.position: int = 11
        self.animal: consts.Animal = consts.Animal.Kangaroo
        self.name: str = name
        self.score: int = 0

        self.total_wins = 0
        self.total_points_for = 0
        self.total_points_against = 0

        if table == []:
            self.init_random_table()
        else:
            self.load_table(table)

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

    def load_table(self, table):
        # set blank table
        self.state_table = []
        for i in range(7):
            col = [0,0,0,0,0]
            self.state_table.append(col)
        
        # convert colors
        color_rows = [0,2]
        for n in color_rows:
            for i in range(7):
                self.state_table[i][n] = consts.Color.Yellow if table[i][n] == 'y' else consts.Color.Green

        # convert animals
        animal_rows = [1, 3]
        for n in animal_rows:
            for i in range(7):
                if (table[i][n] == 'k'):
                    self.state_table[i][n] = consts.Animal.Kangaroo
                if (table[i][n] == 'e'):
                    self.state_table[i][n] = consts.Animal.Emu
                if (table[i][n] == 'w'):
                    self.state_table[i][n] = consts.Animal.Wombat
                if (table[i][n] == 'p'):
                    self.state_table[i][n] = consts.Animal.Platypus

        # convert plant
        for i in range(7):
            self.state_table[i][4] = consts.Plant.GumTree if table[i][4] == 'gg' else consts.Plant.Wattle


    def reset(self):
        self.animal = consts.Animal.Kangaroo
        self.score = 0
        self.position = 11

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
        return str(self.animal)[len("Animal."):len("Animal.")+1]