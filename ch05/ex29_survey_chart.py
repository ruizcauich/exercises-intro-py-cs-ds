import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from ex28_survey_response_statistics import rates

survey_rates, counts = np.unique(rates, return_counts=True)

title = 'Students survey'

sns.set_style('whitegrid')
axes = sns.barplot(x=survey_rates, y=counts, palette='bright')
axes.set_title(title)
axes.set(xlabel='Survey rates', ylabel='Rate frequency')
axes.set_ylim(top=max(counts)*1.20)

for bar, frequency in zip(axes.patches, counts):
    text_x_position = bar.get_x() + bar.get_width() / 2.0
    text_y_position = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rates):.3%}'
    axes.text(text_x_position, text_y_position, text,
              fontsize=11, ha='center', va='bottom')

plt.show()
