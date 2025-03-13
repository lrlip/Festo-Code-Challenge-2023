# Chapter two

import math
import numpy as np
from fractions import Fraction
from utils.egyptian_fraction import EgyptianFraction


def read_trap_file(filename: str):
    with open(filename, 'r') as f:
        trap_list = f.read().splitlines()
    return trap_list


trap_list = read_trap_file(filename='static/23_trap_right_side.txt')

traps_not_balanced_list = read_trap_file(
    filename='static/23_traps_not_balanced.txt')
traps_balanced_list = read_trap_file(
    filename='static/23_traps_balanced.txt')

traps_chapter_2 = split_trap_list(trap_list=trap_list)
traps_not_balanced = split_trap_list(traps_not_balanced_list)
traps_balanced = split_trap_list(traps_balanced_list)


def is_items_equal(trap: list) -> bool:
    """ Equality: Both sides of the scale must contain the same number of objects."""
    return len(trap[0]) == len(trap[1])


def is_weight_equal(trap):
    trap_left = trap[0]
    trap_right = trap[1]
    left_weight = sum(Fraction(1, flask) for flask in trap_left)
    right_weight = sum(Fraction(1, flask) for flask in trap_right)
    print(left_weight, right_weight)
    return left_weight == right_weight


def left_weight(trap):
    sum_weight = sum(Fraction(1, flask) for flask in trap[0])
    return sum_weight


def is_weight_diverse(trap: list) -> bool:
    "Diversity: All objects on the scale must have different weights. No two objects may have the same weight."
    trap_weight = trap[0] + trap[1]
    len_traps = len(trap_weight)
    len_set_traps = len(set(trap_weight))
    print(len_traps, len_set_traps)
    return len_traps == len_set_traps


def get_fraction(list: list):
    nominator = sum(list)
    denominator = np.prod(list)
    return nominator, denominator


def prime_factors(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

    return nom, denom


def greedy_egyptian_fractions(num, denom, ):
    # Greedy egyptian fraction method
    factors = []

    while num != 0:
        # Greates unit factor less than nom/denom = X
        x = math.ceil(denom/num)
        factors.append(x)

        num = x * num - denom
        denom = denom * x
        print(num)

    return factors


traps = traps_not_balanced

for trap_idx in traps:
    trap = traps.get(trap_idx)
    left = trap['left']

    num, denom = get_fraction(left)

    nom_prime = prime_factors(num)
    denom_prime = prime_factors(denom)

    factors = greedy_egyptian_fractions(num, denom)
    fnum, fdenom = get_fraction(factors)

    print('left', left, Fraction(num, denom))
    print('factors:', factors, Fraction(fnum, fdenom))
    # if nom_prime[-1] > denom_prime[-1]:
    #     print('False')

    frac = Fraction(num, denom)

    print(frac)
