# -*- coding: utf-8 -*-
"""
Features selection based on genetic algorithm
"""
import logging
import numpy as np

__author__ = "Rodolfo Dollinger"
__license__ = "mit"

_logger = logging.getLogger()

class ga_selection:
    
    def __init__(self):
        pass
    
    def pop_generation(self, data, pop_size = 10):
        """
        Pop Generation function. Generates a initial population

        Args:
        data (np): input data
        pop_size (int): population size

        Returns:
        pop: generated population
        """
        qtd_var = data.shape[1] - 1
        pop = np.random.randint(2, size=(pop_size, qtd_var))
        return(pop)
    
    def cal_regression(self):  
        # Function to calculate fiting model for regression 
        pass
    
    def cal_classifier(self):
        # Function to calculate fiting model for classification 
        pass
    
    def select_parents(self):
        # Select more adaptable elements
        pass
    
    def crossover(self):
        pass
       
    def mutation(self):
        pass

    def main(self):
        pass