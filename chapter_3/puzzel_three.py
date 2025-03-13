# Chapter three

import numpy as np
from fractions import Fraction


def read_trap_file(filename: str):
    with open(filename, 'r') as f:
        trap_list = f.read().splitlines()
    return trap_list


def split_trap_list(trap_list: list):
    # split trap list for chapter 2

    traps = {}
    for idx, trapline in enumerate(trap_list):
        try:
            _, trap = trapline.strip().split(': ')
        except ValueError:
            trap = trapline.strip()

        left, right = trap.strip().split(' - ')
        l_weights = list(map(int, left.split()))
        r_weights = list(map(int, right.strip().replace(
            '(', '').replace(')', '').split()))
        trap_info = {idx + 1: {'left': l_weights,
                               'right': r_weights}
                     }
        traps.update(trap_info)

    return traps


trap_list = read_trap_file(filename='static/33_trap_water.txt')
traps = split_trap_list(trap_list=trap_list)


def get_combinations(flask):
    """Get all combinations of a flask with water. the combination is a list of fractions.
    loop through the flask and substract all possible items in flask from flask

    e.g.: if flask contains 2, 3. than the possible fraction combinations are:
        1/2, 1/3, 1/2 - 1/3 = 1/6
    """
    flask_combinations = []
    for idx, item in enumerate(flask):
        flask_combinations.append(Fraction(1, item))
        for item2 in flask[idx + 1:]:
            flask_combinations.append(Fraction(1, item) - Fraction(1, item2))
    return set(flask_combinations)


def get_fraction(list: list):
    print(list)
    nominator = sum(list)
    denominator = np.prod(list)
    print(nominator, denominator)
    return Fraction(nominator, denominator)


print(traps[3], get_fraction(traps[3]['left']),
      get_combinations(traps[3]['right']))


def solve():
    """Solve for all traps if the get_fraction of the left side can be made by adding fractions received
    from the get_combinations of the right side
    example 1:
    trapLeft = 6, trapright = 2,3
    1/6 can be made by 1/2 - 1.3
        is True

    example 2:
    trapleft = 2, trapright = 6
    1/2 can be made by 1/6 + 1/6 + 1/6 
        True

    example 3:"
    trapleft = 1/3, trapright = 1/4
    1/3 can not be made by 1/4
        False

    """
