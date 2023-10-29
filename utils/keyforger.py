import time
import functools
from collections import deque
import datetime
from typing import Any


class KeyForger:

    def __init__(self, filename) -> None:
        self.filename = filename
        self.hammers = self.import_hammer_collection()
        # self.recipes = self.import_hammer_recipe()
        self.keys = self.read_keys()
        self.start_time = datetime.datetime.now()
        self.key_queue = deque(self.keys)
        self.key_queue.reverse()
        self.key = None

    def import_hammer_collection(self) -> dict():
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

    def read_keys(self):
        """Read keys from file"""
        with open(self.filename, 'r') as file:
            keys = file.read().splitlines()
        return keys

    def string_E_needs_an_F(self, key):
        """in a key, an E can only exist when it it has a F as prefix
        replace all FE with C if allowed

        Args:
            key (str): keystring

        Returns:
            key: _description_
        """
        res_E = [i for i in range(len(key)) if key.startswith('E', i)]
        res_FE = [i for i in range(len(key)) if key.startswith('FE', i)]

        if len(res_E) == len(res_FE):
            key = key.replace('FE', 'C')
            return key
        else:
            return None

    def string_A_needs_an_F(self, key):
        """When A exists, it needs to be an AF or FA

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        res_A = [i for i in range(len(key)) if key.startswith('A', i)]
        res_AF = [i for i in range(len(key)) if key.startswith('AF', i)]
        res_FA = [i for i in range(len(key)) if key.startswith('FA', i)]

        res_AF_FA = set(res_AF + [idx + 1 for idx in res_FA])

        # Every A needs a AF or an FA so length A cannot be bigger than set of FA, AF
        if len(res_A) > len(res_AF_FA):
            return None

        return key

    @functools.cache
    def check_key(self, key: str) -> bool:
        """Check if a key is valid"""

        if len(key) == 1:
            # Length 1 must be A
            return key[0] == 'A'

        key = self.string_E_needs_an_F(key)
        if key == None:
            return False

        key = self.string_A_needs_an_F(key)
        if key == None:
            return False

        if key:
            for idx in range(len(key) - 1):
                output = key[idx] + key[idx+1]

                # If hammer exist, assign letter
                if letter := self.hammers.get(output):
                    new_key = self.replace_hammer_key(key, idx, letter)
                    if new_key == None:
                        continue

                    if self.check_key(new_key):
                        return True
                    else:
                        continue
                else:
                    continue

    def replace_hammer_key(self, key, idx, replacement):
        """Replace the string of the key with the hammer

        Args:
            key (str): ke
            idx (int): location of the hammer   
            replacement (str): the hammer that is used to force the key

        Returns:
            _type_: _description_
        """
        return key[:idx] + replacement + key[idx+2:]

    def solve(self, show_idx=False):
        """Solver for the key

        Returns:
            key: the key that is valid
        """
        idx = 0
        while self.key_queue:
            key = self.key_queue.pop()
            if show_idx:
                print(idx := idx + 1)

            if self.check_key(key):
                self.key = key
                break
        return self.key
