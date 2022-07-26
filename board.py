from typing import List
import consts


class Board:
    size: int = consts.board_size
    state: List[consts.Color] = []

    def __init__(self):
        self.state = [consts.Color.Yellow] * self.size

    def print_board(self):
        string = ""
        for char in self.state:
            s = "Y" if char == consts.Color.Yellow else "G"
            string += s
        print(string)
