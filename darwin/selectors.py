__author__ = 'avathar'

import random


class RankSelector(object):
    def __init__(self, maximize):
        self.maximize = maximize

    def select_pairs(self, population):
        pop_size = len(population)
        parent_size = pop_size / 2

        # sort population by rank
        population.sort(key=lambda x: x.fitness, reverse=self.maximize)

        # select top half of the population
        parent_pool = population[0:len(population)/2]
        # make pairs
        parents = []
        while len(parents) < parent_size:
            random_1 = random.randint(0, len(parent_pool)-1)
            random_2 = random.randint(0, len(parent_pool)-1)
            parent_1 = parent_pool[random_1]
            parent_2 = parent_pool[random_2]
            parents.append([parent_1, parent_2])
        return parents
