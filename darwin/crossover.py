__author__ = 'avathar'

import random


class CrossOver(object):
    """
    Base class, not to be used
    """
    @classmethod
    def recombine(cls, list_1, list_2):
        """
        returns elements
        """
        return list_1, list_2


class OnePointCrossover(CrossOver):
    """
    OnePointCrossover:
    """

    @classmethod
    def recombine(cls, list_1, list_2):
        """
        - swaps list elements to right of randomized crossover point
        """
        # determine crossover point
        max_val = len(list_1)
        crossover_point = random.randint(1, max_val - 1)

        # perform crossover
        child_1 = list_1[0:crossover_point] + list_2[crossover_point:]
        child_2 = list_2[0:crossover_point] + list_1[crossover_point:]

        return child_1, child_2
