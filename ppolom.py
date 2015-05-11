__author__ = 'avathar'

import json
import numpy as np
from darwin.ga import GeneticAlgorithm
from darwin.genotype import Genotype
from darwin.fitness import FitnessFunction

item = '1005.90.03'


def read_distance():
    with open('distances.json', 'r') as input_file:
        distances = json.load(input_file)
        data = {}
        for country in distances:
            data[country['id']] = {
                "country": country['country'],
                "distance": country['distance']
            }
        return data


def read_file(filename):
    with open(filename, 'r') as input_file:
        return json.load(input_file)


class PpolomFitness(FitnessFunction):
    def __init__(self):
        self.distances = read_distance()
        self.trade_agreements = read_file('trade_agreements.json')
        self.quotas = read_file('quotas.json')
        self.products = read_file('products.json')

    def evaluate(self, chromosome):
        country_code = chromosome.genes[0]
        quantity = chromosome.genes[1]
        tax = 0
        item_fta = None
        item_quota = 0
        # get distance to country
        country_distance = self.distances[country_code]['distance']
        # find tax for product
        for fta, countries in self.trade_agreements.items():
            if country_code in countries:
                tax = self.products[item]['fta'][fta]
                item_fta = fta
            else:
                tax = self.products[item]['tax']
        if tax is None:
            tax = self.products[item]['tax']
        if item in self.quotas:
            item_quota = self.quotas[item]['quota']
            if not isinstance(item_quota, int):
                if item_fta is not None and item_fta in item_quota:
                    item_quota = self.quotas[item]['quota'][item_fta]
                else:
                    item_quota = 0

        quota_delta = abs(item_quota - quantity)
        fitness_value = country_distance + quota_delta + (tax*quota_delta)
        return fitness_value


def run():

    ppplom_fitness = PpolomFitness()

    labels = [
        'code',
        'units',
    ]
    values = [
        [code for code in ppplom_fitness.distances.keys()],
        [i for i in range(1000, 10000000, 1000)]
    ]

    sample = Genotype(labels, values)
    ga = GeneticAlgorithm(population_size=200,
                          sample_genotype=sample,
                          crossover_rate=0.6,
                          mutation_rate=0.02,
                          maximize=False)
    best_generation = ga.evolve(fitness_obj=ppplom_fitness,
                                num_generations=500)

    print "Best Generation "
    all_fitness = []
    for chrom in best_generation:
        all_fitness.append(chrom.fitness)

    fittest = ga.best_individual(best_generation)

    results = [
        ('Product', ppplom_fitness.products[item]['product']),
        ('Country', ppplom_fitness.distances[fittest['code']]['country']),
        ('Units', fittest['units']),
        ('Avg fitness value', np.average(all_fitness)),
        ('Max fitness value', np.max(all_fitness)),
        ('Min fitness value', np.min(all_fitness)),
        ('Std fitness value', np.std(all_fitness))
    ]

    return results
