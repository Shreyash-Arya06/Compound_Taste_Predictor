import numpy as np
import os
from genetic_algorithm import *

def main():
    result_path = 'dataset/calculated_weights/weights_iterations.txt'
    if os.path.exists(result_path):
        open_method = 'a' # append if already exists
    else:
        open_method = 'w' # make a new file if not

    file = open(result_path, open_method)
    file.write('#----------New iteration started.----------#\n')
    file.close()

    Genetic_Algo = Genetic(size_of_group = 20, max_generation = 100)
    best_chromosome = Chromosome()

    best_chromosome = Genetic_Algo.run()

    result_path = 'dataset/calculated_weights/best_weights.txt'
    if os.path.exists(result_path):
        open_method = 'a' # append if already exists
    else:
        open_method = 'w' # make a new file if not
    file = open(result_path, open_method)
    file.write(f'cost: {np.round(best_chromosome.genes, 8)}, fitness: {round(best_chromosome.fitness, 8)}\n')
    file.close()

    result_path = 'dataset/calculated_weights/weights_iterations.txt'
    file = open(result_path, 'a')
    file.write('#----------Iteration finished.----------#\n')
    file.close()

main()