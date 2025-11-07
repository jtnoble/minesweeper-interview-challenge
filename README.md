# Minesweeper Interview Challenge
Basic Minesweeper interview challenge.

## Problem
Given a string, separated by newline characters, identify the amount of mines around a space. Return a string where all non-mine spaces are replaced with the number of mines adjacent to the space.

For example:

```
INPUT:

*...
....
.*..
....

OUTPUT:

*100
2210
1*10
1110

```

## Setup
- `python3 -m venv .venv`
    - Create a virtual environment
- `source .venv/bin/activate`
    - Activate virtual environment
- `make init`
    - Build the project

## Run Commands
- `make verify`
    - run tests
- `make run`
    - run `main.py`

### Other Notes
- The initial commit for this repository is where I personally was at by the end of the interview. The newest commit is changes after my interview experience.