import numpy as np
import scipy.stats as stats

#  Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего
# роста родителей и детей.

mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])

dif_means = np.mean(mothers) - np.mean(daughters)
std_error = np.sqrt(np.var(mothers, ddof=1) / len(mothers) + np.var(daughters, ddof=1) / len(daughters))
t_crit = stats.t.ppf(0.975, len(mothers) + len(daughters) - 2)
A = dif_means - t_crit * std_error
B = dif_means + t_crit * std_error

print(f'95% доверительный интервал для разности среднего роста родителей и детей: [{A:.3f}, {B:.3f}]')
