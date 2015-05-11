__author__ = 'avathar'

import random


class Mutation(object):
    def __init__(self):
        pass

    def mutate(self, genotype, population):
        pop_size = len(population)
        indexes = random.sample([_ for _ in range(pop_size)], pop_size/3)
        for i in indexes:
            population[i] = genotype.create_random_instance()

        return population