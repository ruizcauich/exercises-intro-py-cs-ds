import sys
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

coin_flips_number = 200

if __name__ == '__main__':
    try:
        coin_flips_number = int(sys.argv[1])
        print(f'Simulating {coin_flips_number} coin flips.')
    except:
        print('No numeric argument was provided.\n'
              'Setting 200 as default number of coin flips.')

coin_flips_results = [random.randrange(1, 3) for i in range(coin_flips_number)]

coin_faces, counts = np.unique(coin_flips_results, return_counts=True)

sns.set_style('whitegrid')
axes = sns.barplot(x=coin_faces, y=counts, palette='bright')
axes.set_title('Coin tossing')
axes.set(xlabel='Values', ylabel='Frequencies')
axes.set_ylim(top=max(counts) * 1.20)

for bar, frequency in zip(axes.patches, counts):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / coin_flips_number: .3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

plt.show()
