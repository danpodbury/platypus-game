import machine
import board


if (__name__ == "__main__"):
    print("Welcome to Platypus game")

    b = board.Board()
    b.print_board()

    p = machine.Machine("bot01")
    p.print_table()
