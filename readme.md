# Platypus Game

A deritive of the [Busy Beaver game](https://en.wikipedia.org/wiki/Busy_beaver). It consists of two turing machines that compete to flip the most cells before one of them halts.


## Rules of the game:
- There are two machines
- Machines start as kangaroos
- There is a board with 21 cells
- Each machine begins at cell 11
- All cells are initally yellow
- Each turn a machine reads its animal, and the colour of its cell
- The machine's action is determined from this combination
- The machine will do 3 things as a result:
    - change the current cell to either yellow or green
    - change its animal
    - move left or right
- If a machine changes the colour of its cell it scores a point
- The game halts when a machine is on a green cell, and its animal is a playpus


## Data processing

A textfile of machines has been provided. However it is designed to run in prolog. The `data` module extracts and converts this infomation into a usable list of machine objects.


## Gamemodes

There are two selctable gamemodes: 
- `Single_match` will generate two random machines to compete.
- `Tournament` imports the machines from the provided file, and runs competitions until every combination of machines have battled.


## How to run

`python main.py [ single | tournament ]`


## Sample output
```
Welcome to Platypus game
         K
YYYYYYYYYYYYYYYYYYYYY
         K
---------------------
Bot_01's turn.
          K
YYYYYYYYYYYYYYYYYYYYY
         K
---------------------
Bot_02's turn.
          K
YYYYYYYYYYYYYYYYYYYYY
        W
---------------------
Bot_01's turn.
           K
YYYYYYYYYYYYYYYYYYYYY
        W
---------------------
Bot_02's turn.
           K
YYYYYYYYYYYYYYYYYYYYY
       P
---------------------
        .
        .
        .
---------------------
Bot_01's turn.
      K
YYYYYYYYGGYYYYYYYYYYY
        E
---------------------
Bot_02's turn.
      K
YYYYYYYYGGYYYYYYYYYYY
       K
---------------------
Bot_01's turn.
Bot_01 scored!
       P
YYYYYYYGGGYYYYYYYYYYY
       K
---------------------
Bot_02's turn.
       P
YYYYYYYGGGYYYYYYYYYYY
        E
---------------------
Bot_01's turn.
Bot_01 drew a green platypus! This ends the game.
Scores:
Bot_01: 1
Bot_02: 2
```