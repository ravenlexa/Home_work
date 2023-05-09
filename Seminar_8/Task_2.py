import numpy as np
from scipy import stats

# Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

iq = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]

iq_average = np.mean(iq)
D = np.var(iq, ddof=1)
t = stats.t.ppf(0.975, (len(iq) - 1))
left = round(iq_average - t * np.sqrt(D / len(iq)), 2)
right = round(iq_average + t * np.sqrt(D / len(iq)), 2)

print(f'Доверительный интервал для математического ожидания с надежностью 0.95: [{left}; {right}]')
