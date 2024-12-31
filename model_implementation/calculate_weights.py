import numpy as np
import os
from models.genetic_algorithm import *

def main():
    Genetic_Algo = Genetic()
    best_chromosome = Chromosome()

    best_chromosome = Genetic_Algo.run()
    
    result_path = 'dataset/calculated_weights/best_weights.txt'
    if os.path.exists(result_path):
        open_method = 'a' # append if already exists
    else:
        open_method = 'w' # make a new file if not
    file = open(result_path, open_method)
    file.write(f'cost: {np.round_(best_chromosome.genes, 8)}, fitness: {round(best_chromosome.fitness, 8)}\n')
    file.close()

main()