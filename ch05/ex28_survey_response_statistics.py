import statistics
import numpy as np

rates = [1, 2, 5, 4, 3,
         5, 2, 1, 3, 3, 
         1, 4, 3, 3, 3, 
         2, 3, 3, 2, 5]

print(f'{"Rate":<6} {"Count":<6}')
uniques_and_counts = np.unique(rates, return_counts=True)
uniques_and_counts = zip(uniques_and_counts[0], uniques_and_counts[1])

for rate, count in uniques_and_counts:
    print(f'{rate:<6} {count:<6}')


print(f'{"Minimum:":<15}{min(rates)}')
print(f'{"Maximum:":<15}{max(rates)}')
print(f'{"Range:":<15}{(max(rates) - min(rates))}')
print(f'{"Mean:":<15}{statistics.mean(rates)}')
print(f'{"Median:":<15}{statistics.median(rates)}')
print(f'{"Mode:":<15}{statistics.mode(rates)}')
print(f'{"Variation:":<15}{statistics.variance(rates)}')
print(f'{"Std Deviation:":<15}{statistics.stdev(rates)}')
