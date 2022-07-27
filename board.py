from typing import List
import consts


class Board:
    def __init__(self):
        self.cells: List[consts.Color] = [consts.Color.Yellow] * consts.board_size

    def print_board(self):
        string = ""
        for char in self.cells:
            s = "Y" if char == consts.Color.Yellow else "G"
            string += s
        print(string)
