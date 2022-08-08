from time import time_ns
from typing import List
import machine
import board
import consts

def run_single_match(m1: machine.Machine, m2: machine.Machine, printing=True):
    def increment_turn(n: int) -> int:
        return 0 if (n+1 > 1) else n+1 

    def print_board():
        left_pad = " " * (machines[0].position - 2)
        display(left_pad + machines[0].render_animal())
        if printing: 
            _board.print_board()
        left_pad = " " * (machines[1].position - 2)
        display(left_pad + machines[1].render_animal())
        display("-"*consts.board_size)

    def display(string: str):
        if printing:
            print(string)

    # Initalise Game State
    turn:int = 0
    current_machine:int = 0
    _board = board.Board()

    # Init machines
    machines: List[machine.Machine] = [m1, m2]
    m1.reset()
    m2.reset()

    print_board()

    # Enter Game Loop
    max_iter = 100
    playing:bool = True    
    while playing:

        # Begin turn
        display("%s's turn." % machines[current_machine].name)

        # read cell
        machine_position = machines[current_machine].position
        cell_color:consts.Color = _board.cells[machine_position]

        # get current machine state/animal
        current_state:consts.Animal = machines[current_machine].animal

        # check for endgame condition
        if (cell_color == consts.Color.Green and current_state == consts.Animal.Platypus):
            playing = False
            display("%s drew a green platypus! This ends the game."% machines[current_machine].name)
            break

        # save current state for scoring
        prev_pos = machine_position - 1
        prev_color = _board.cells[prev_pos]

        # determine new animal and colour
        [new_color, new_animal, move_direction] = machines[current_machine].make_decision(cell_color)

        # update cell state/colour
        _board.cells[prev_pos] = new_color

        # update machine state
        machines[current_machine].animal = new_animal
        if (move_direction == "<"):
            machines[current_machine].move_left()
        else:
            machines[current_machine].move_right()

        # if move changes colour increment score
        if (prev_color != new_color):
            machines[current_machine].score += 1
            display("%s scored!" % machines[current_machine].name)

        # End turn
        current_machine = increment_turn(current_machine)

        # increment turn when both players have made a move
        if current_machine == 1:
            turn += 1

        # bail out if we don't halt after 100 turns
        if (turn > max_iter):
            playing = False
            display("Hit max iterations!")
            break

        print_board() 

    # Print scores once game is complete
    display("Scores:")
    display("%s: %s\n%s: %s" % (machines[0].name, machines[0].score, machines[1].name, machines[1].score))
    return [machines[0].score,  machines[1].score]

def run_tournament(machines: List[machine.Machine]):
    print("Running tournament...")

    t1 = time_ns()
    matches_played=0

    # each machine battles every other only once
    for i in range(268):
        for j in range(i+1, 268):
            # make em fight
            [i_score, j_score] = run_single_match(machines[i], machines[j], printing=False)

            # update total score
            machines[i].total_points_for = i_score
            machines[i].total_points_against = j_score

            machines[j].total_points_for = j_score
            machines[j].total_points_against = i_score           

            # update total wins
            if (i_score > j_score):
                 machines[i].total_wins += 1
            if (j_score > i_score):
                 machines[j].total_wins += 1

            # count match
            matches_played += 1

    print("Done.")
    print("(Ran %d matches in %.2f seconds)" % (matches_played, (time_ns() - t1)/1e9))

    with open('output.csv', 'w') as file:
        file.write("Number, Wins, For, Against\n")
        for i, m in enumerate(machines):
            file.write(str(i)+", "+str(m.total_wins)+", "+ \
                    str(m.total_points_for)+", "+str(m.total_points_against) + "\n")
