from typing import List
import machine
import board
import consts

def run_single_match():
    def increment_turn(n: int) -> int:
        return 0 if (n+1 > 1) else n+1 

    def print_board():
        left_pad = " " * (machines[0].position - 2)
        print(left_pad,  machines[0].render_animal())
        _board.print_board()
        left_pad = " " * (machines[1].position - 2)
        print(left_pad, machines[1].render_animal())
        print("-"*consts.board_size)

    # Initalise Game State
    turn:int = 0
    current_machine:int = 0
    _board = board.Board()

    # Create machines
    machines: List[machine.Machine] = [machine.Machine("bot01"), 
                                       machine.Machine("bot02")]

    print_board()

    # Enter Game Loop
    max_iter = 100
    playing:bool = True    
    while playing:

        # Begin turn
        print("%s's turn." % machines[current_machine].name)

        # read cell
        machine_position = machines[current_machine].position
        cell_color:consts.Color = _board.cells[machine_position]

        # get current machine state/animal
        current_state:consts.Animal = machines[current_machine].animal

        # check for endgame condition
        if (cell_color == consts.Color.Green and current_state == consts.Animal.Platypus):
            playing = False
            print("%s drew a green platypus! This ends the game."% machines[current_machine].name)
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
            print("%s scored!" % machines[current_machine].name)

        # End turn
        current_machine = increment_turn(current_machine)

        # increment turn when both players have made a move
        if current_machine == 1:
            turn += 1

        # bail out if we don't halt after 100 turns
        if (turn > max_iter):
            playing = False
            print("Hit max iterations!")
            break

        print_board() 

    # Print scores once game is complete
    print("p1: " + str(machines[0].score) + ", p2: " +  str(machines[1].score))

def run_tournament(machines):
    print(len(machines))