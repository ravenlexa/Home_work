import numpy as np
import scipy.stats as stats
# Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции, имеются ли статистические различия между группами?

alpha = 0.05
x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])

stat = stats.mannwhitneyu(x1, y1)
print(stat)
print('pvalue > alpha, H0 - не отвергается, cтатистически значимых различий нет!')

