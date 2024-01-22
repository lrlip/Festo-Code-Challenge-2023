import numpy as np


def import_trap_balance(filename: str = None,
                        dict_list: str = None):
    """Import the trap balanced

    Returns:
        dict[list,] {1: [[a, b], [c, d]], 2: [[e, f, g][h, i]] }
    """
    trap_list = {}
    if filename:
        with open(filename, 'r') as f:
            dict_list = f.read().splitlines()

    for line in dict_list:
        # print(line)
        logline = line.strip()

        line_idx_line = line.strip().split(': ')
        idx = line_idx_line[0]
        # print(line_idx_line)
        if line_idx_line:
            line_lr = line_idx_line[1].split(' - ')
            left = [int(val) for val in line_lr[0].split()]
            right = [val for val in line_lr[1].split()]
            trap_list[int(idx)] = [left, right]

    return trap_list


def prime_factors(value):
    d = 2
    primes = []
    while d * d <= value:
        if value % d:
            d += 1
        else:
            value //= d
            primes.append(d)
    if d > 1:
        primes.append(d)
    return primes


def get_correct_traps():
    """A trap is correct if it is possible to find another pair of weights that can achieve the same 
    total weight.
    To find such traps we use prime factorization nominator and denominator.
    If the max prime factor in the nominator > max(prime(denominator)) an other option is not possible
    """
    traplist = import_trap_balance(
        filename="static/23_trap_right_side.txt")

    sum = 0
    for key in traplist:
        trap = list(traplist.get(key)[0])

        primes = []
        frac_sum = np.sum(trap)
        frac_mult = np.prod(trap)
        # print(frac_sum)
        sum_prime = prime_factors(frac_sum)
        mult_prime = prime_factors(frac_mult)
        print(sum_prime, mult_prime)
        if np.max(sum_prime) >= np.max(mult_prime):
            print(sum_prime, mult_prime, False)
        else:
            print(sum_prime, mult_prime, True)

            sum += key
    return sum


idx_sum = get_correct_traps()
print(f'the total sum is {idx_sum}')
