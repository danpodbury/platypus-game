from typing import List
import machine
import gamemodes
import data

if (__name__ == "__main__"):
    print("Welcome to Platypus game")

    machines: List[machine.Machine] = data.extract_machines("./machine_list.txt")
    #gamemodes.run_single_match()
    gamemodes.run_tournament(machines)
