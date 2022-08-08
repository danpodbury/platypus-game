from typing import List
import machine
import gamemodes
import data
import sys

def print_usage():
    print("Invalid arguments")
    print("Usage:")
    print("> python main.py [ single | tournament ]")    

def print_welcome():
    print("Welcome to Platypus game")

if (__name__ == "__main__"):
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "single":
            print_welcome()
            gamemodes.run_single_match(machine.Machine("Bot_01"), machine.Machine("Bot_02"))
        elif sys.argv[1] == "tournament":
            print_welcome()
            machines: List[machine.Machine] = data.extract_machines("./machine_list.txt")
            gamemodes.run_tournament(machines)
        else:
            print_usage()

    else:
        print_usage()
