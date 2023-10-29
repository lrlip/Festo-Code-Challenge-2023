import time
import functools
from collections import deque
import datetime
from typing import Any


def import_hammer_collection() -> dict():
    """Import the Hammer collection from file

    Returns:
        dict: dict containg the collection of hammers
    """
    hammer_collection = {}
    with open('static\hammer_collection.txt', 'r') as f:
        for line in f:
            number_hammer = line.split('. ')
            before_after = number_hammer[1].strip().split(' -> ')
            hammer_collection[before_after[1]] = before_after[0]
    return hammer_collection


def read_keys():
    with open('static/31_keymaker_forge_2.txt', 'r') as file:
        keys = file.read().splitlines()
    return keys


@functools.cache
def check_key(key: str) -> bool:

    if len(key) == 1:
        # Length 1 must be A
        return key[0] == 'A'

    key = string_E_needs_an_F(key, hammers=hammers)
    if key == None:
        return False

    key = string_A_needs_an_F(key, hammers=hammers)
    if key == None:
        return False

    if key:
        for idx in range(len(key) - 1):
            output = key[idx] + key[idx+1]

            # If hammer exist, assign letter
            if letter := hammers.get(output):
                new_key = replace_hammer_key(key, idx, letter)
                if new_key == None:
                    continue

                if check_key(new_key):
                    return True
                else:
                    continue
            else:
                continue


def replace_hammer_key(key, idx, replacement):
    return key[:idx] + replacement + key[idx+2:]


def string_E_needs_an_F(key, hammers):

    res_E = [i for i in range(len(key)) if key.startswith('E', i)]
    res_FE = [i for i in range(len(key)) if key.startswith('FE', i)]

    if len(res_E) == len(res_FE):
        key = key.replace('FE', 'C')
        return key
    else:
        return None


def string_A_needs_an_F(key, hammers):
    res_A = [i for i in range(len(key)) if key.startswith('A', i)]
    res_AF = [i for i in range(len(key)) if key.startswith('AF', i)]
    res_FA = [i for i in range(len(key)) if key.startswith('FA', i)]

    res_AF_FA = set(res_AF + [idx + 1 for idx in res_FA])

    # Every A needs a AF or an FA so length A cannot be bigger than set of FA, AF
    if len(res_A) > len(res_AF_FA):
        return None

    return key


hammers = import_hammer_collection()
keys = read_keys()

for idx, key in enumerate(keys):
    print(idx)
    if check_key(key):
        print(key)
