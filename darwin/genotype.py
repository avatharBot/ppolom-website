__author__ = 'avathar'

import random
from chromosome import Chromosome


class Genotype(object):
    """
    Genotype defines the structure of a chromosome
    """
    def __init__(self, labels, values):
        self.labels = labels
        self.values = values

    def describe(self):
        """
        describe: tuple with genotype info
        """
        description = (len(self.values), self.labels, self.values)
        return description

    def num_genes(self):
        """
        num_genes: # genes in genotype
        """
        return len(self.values)

    def create_random_instance(self):
        """
        create_random_instance: creates chromosome with randomized gene values
        """
        instance = []
        for each in self.values:
            num = len(each) - 1
            index = random.randint(0, num)
            gene_value = each[index]
            instance.append(gene_value)

        chromosome = Chromosome(genes=instance)
        return chromosome

    def get_label_at(self, pos):
        """
        get_label: label from gene position
        """
        return self.labels[pos]
