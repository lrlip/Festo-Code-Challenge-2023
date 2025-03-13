from fractions import Fraction
import numpy as np
from utils.egyptian_fraction import EgyptianFraction


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
        r_weights = right.strip().split()
        trap_info = {idx + 1: {'left': l_weights,
                               'right': r_weights}
                     }
        traps.update(trap_info)

    return traps


def get_fraction(fraction_list: list):
    fraction = 0
    for flask in fraction_list:
        fraction += Fraction(1, flask)
    return fraction


def get_num_denom(left_list: list):

    fraction = get_fraction(left_list)
    nominator = fraction.numerator
    denominator = fraction.denominator

    return nominator, denominator


def get_valid_trap(trap: list):
    min_factor = 2
    num, denom = get_num_denom(trap)
    egyptians = EgyptianFraction(num, denom)

    # Start loop
    for i in range(100):
        factors = egyptians.greedy_egyptian_fractions(min_factor=min_factor,
                                                      max_length=len(left))
        if factors:
            if len(factors) == len(left):
                for item in factors:
                    if item in left:
                        continue

                    else:
                        return factors
        min_factor = min_factor + 1

    return None


def get_valid_trap_next(trap: list):
    min_factor = 2
    num, denom = get_num_denom(trap)
    egyptians = EgyptianFraction(num, denom)

    # Start loop
    print(trap)
    factor = egyptians.next_egyptian_fraction(num=num,
                                              denom=denom,
                                              min_factor=min_factor)

    print(factor)

    if factor in trap:
        min_factor = factor + 1
        factor = egyptians.next_egyptian_fraction(num=num,
                                                  denom=denom,
                                                  min_factor=min_factor)

    if factors:
        if len(factors) == len(left):
            for item in factors:
                if item in left:
                    continue

                else:
                    return factors
    min_factor = min_factor + 1

    return None


trap_list = read_trap_file(filename='static/23_trap_right_side.txt')

traps_not_balanced_list = read_trap_file(
    filename='static/23_traps_not_balanced.txt')
traps_balanced_list = read_trap_file(
    filename='static/23_traps_balanced.txt')

traps_chapter_2 = split_trap_list(trap_list=trap_list)
traps_not_balanced = split_trap_list(traps_not_balanced_list)
traps_balanced = split_trap_list(traps_balanced_list)

traps = traps_balanced
sum = 0
for trap_idx in traps:
    left = traps[trap_idx]['left']
    valid = get_valid_trap(trap=left)
    print(valid, left)
    if valid and get_fraction(valid) == get_fraction(left):
        sum += trap_idx
        print(valid)
        print(sum)
