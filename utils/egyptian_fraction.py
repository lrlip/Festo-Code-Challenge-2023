from fractions import Fraction
import math


class EgyptianFraction:

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        self.next_factor = None
        self.fraction = Fraction(num, denom)

    def next_egyptian_fraction(self,
                               num,
                               denom,
                               min_factor: int = None):

        x = math.ceil(denom/num)

        if min_factor:
            if x < min_factor:
                x = min_factor

        return x

    def greedy_egyptian_fractions(self,
                                  min_factor: int = None,
                                  max_length: int = None):
        """Greedy egyptian fraction method
        Args:
            num (int): nominator
            denom (int): denominator
        Returns:
            list: list of factors
        """
        num = self.num
        denom = self.denom
        factors = []

        while num != 0:
            # Greatest unit factor less than nom/denom = X
            x = math.ceil(denom/num)

            factors.append(x)

            if min_factor and x < min_factor:
                x = min_factor

            if len(factors) > max_length:
                return None

            num = x * num - denom
            denom = denom * x

            min_factor += 1

        return factors


if __name__ == '__main__':
    num = 3
    denom = 105
    egyptians = EgyptianFraction(num, denom)
    factor = egyptians.next_egyptian_fraction(min_factor=2)

    egyptians = EgyptianFraction(num, denom)
    factors = egyptians.greedy_egyptian_fractions(min_factor=2)
    print(factor)
    print(factors)
