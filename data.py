from typing import List
import machine

def extract_machines(filename: str) -> List[machine.Machine]:
    print("Extracting machines from file...")

    machines: List[machine.Machine] = []

    # Extract lines from file
    lines = []
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()

    # Extract machine info from each line
    machine_index = 1
    for line in lines:
        # split off table cols
        cols = line.split('[')[1].split(']')[0].split('t')[1:]

        # remove trailing comma
        cols = [c[:-1] for c in cols if c[-1] == ','] + cols[-1:]

        # remove brackets
        cols = [c[1:-1] for c in cols]

        # get individual elems
        machine_table = [c.split(',') for c in cols]

        # parse list into object
        p = machine.Machine("bot_" + str(machine_index), machine_table)
        machines.append(p)

        machine_index += 1

    return machines