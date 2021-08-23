import numpy as np
import random

random_numbers = [random.randrange(1,11) for i in range(50)]
print(f'Random numbers: {random_numbers}')
print('Uniques and frecuencies: ')
print(np.unique(random_numbers, return_counts=True))

