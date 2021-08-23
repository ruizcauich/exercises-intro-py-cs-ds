import sys
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# use list comprehension to create a list of rolls of a six-sided die
rolls = [random.randrange(1, 7) + random.randrange(1, 7)
         for i in range(int(sys.argv[1]))]

# NumPy unique function returns unique faces and frequency of each face
values, frequencies = np.unique(rolls, return_counts=True)

title = f'Rolling two Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')  # white backround with gray grid lines
axes = sns.barplot(frequencies, values, palette='bright', orient='h')  # create bars
axes.set_title(title)  # set graph title
axes.set(xlabel='Frequency', ylabel='Die value')  # label the axes

# scale y-axis by 10% to make room for text above bars
axes.set_xlim(right=max(frequencies) * 1.2)


for bar, frequency in zip(axes.patches, frequencies):
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    text_y = bar.get_y() + bar.get_height() / 2.0
    text_x = bar.get_width()
    axes.text(text_x, text_y, text,
              fontsize=11, ha='left', va='center')

plt.show()  # display graph 


