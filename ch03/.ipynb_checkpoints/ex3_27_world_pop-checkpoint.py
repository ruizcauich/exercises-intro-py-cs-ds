"""Calculate the population of the world for the
next 100 years"""

growth_rate = 0.0105
actual_population = 7794798739

print(f'{"year":>6}{"expected pupulation":>20}{"year growth":>15}')
for n_year in range(1, 101):
    year_growth = actual_population*growth_rate
    actual_population += year_growth
    print(f'{n_year:>6}{actual_population:>20.0f}{year_growth:>15.0f}')