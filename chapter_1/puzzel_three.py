from fractions import Fraction


def import_trap_balance():
    """Import the trap balanced


    Returns:
        dict[list,] {1: [[a, b], [c, d]], 2: [[e, f, g][h, i]] }
    """
    trap_list = {}
    with open("static\\13_trap_balance.txt", 'r') as f:
        for line in f:
            line_idx_line = line.strip().split(': ')
            idx = line_idx_line[0]
            line_lr = line_idx_line[1].split(' - ')
            left = [int(val) for val in line_lr[0].split()]
            right = [int(val) for val in line_lr[1].split()]
            trap_list[int(idx)] = [left, right]

    return trap_list


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


def is_weight_diverse(trap: list) -> bool:
    "Diversity: All objects on the scale must have different weights. No two objects may have the same weight."
    trap_weight = trap[0] + trap[1]
    len_traps = len(trap_weight)
    len_set_traps = len(set(trap_weight))
    print(len_traps, len_set_traps)
    return len_traps == len_set_traps


traplist = import_trap_balance()

test_dict = {1: [[4, 4], [3, 6]],
             2: [[2, 4, 20], [2, 5, 10]],
             3: [[2, 99999999999999999999999999999999999], [3, 6]],
             4: [[4, 20], [5, 10]]}

idx = 0
# traplist = test_dict
for key in traplist:
    if is_items_equal(traplist[key]):
        if is_weight_equal(traplist[key]):
            if is_weight_diverse(traplist[key]):
                print(traplist[key])
                idx += key

print(f'The total value is: {idx}')
