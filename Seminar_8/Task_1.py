import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Даны значения величины заработной платы заемщиков банка (zp) и значения их
# поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с
# помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и
# среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
plt.scatter(zp, ks)
plt.show()

cov_zp_ks = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
print('Ковариация двух величин с помощью элементарных действий:\n', cov_zp_ks)


cov_zp_ks = np.cov(zp, ks, ddof=0)[0, 1]
print('Ковариация двух величин через функцию cov:\n', cov_zp_ks)


corr = cov_zp_ks / (np.std(zp) * np.std(ks))
print('Коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков:\n', corr)

corr_numpy = np.corrcoef(zp, ks)[0][1]
print('Коэффициент корреляции Пирсона с помощью библиотеки numpy:\n', corr_numpy)

corr_pandas = pd.Series(zp).corr(pd.Series(ks), method='pearson')
print('Коэффициент корреляции Пирсона с помощью библиотеки pandas:\n', corr_pandas)

