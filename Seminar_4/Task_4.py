from statistics import NormalDist


# Рост взрослого населения города X имеет нормальное распределение, причем,
# средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см.
# посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# 1. больше 182 см?
# 2. больше 190 см?
# 3. от 166 см до 190 см?
# 4. от 166 см до 182 см?
# 5. от 158 см до 190 см?
# 6. не выше 150 см или не ниже 190 см?
# 7. не выше 150 см или не ниже 198 см?
# 8. ниже 166 см?

# Создадим функцию для поиска Z величины
def z_value(h):
    return (h - 174) / 8


# 1
a = z_value(182)
Pa = 1 - NormalDist().cdf(a)
print('1 = ', Pa)

# 2
b = z_value(190)
Pb = 1 - NormalDist().cdf(b)
print('2 = ', Pb)

# 3
c1 = z_value(166)
c2 = z_value(190)
Pc = NormalDist().cdf(c2)-NormalDist().cdf(c1)
print('3 = ', Pc)

# 4
d1 = z_value(166)
d2 = z_value(182)
Pd = NormalDist().cdf(d2)-NormalDist().cdf(d1)
print('4 = ', Pd)

# 5
e1 = z_value(158)
e2 = z_value(190)
Pe = NormalDist().cdf(e2)-NormalDist().cdf(e1)
print('5 = ', Pe)

# 6
f1 = z_value(150)
f2 = z_value(190)
Pf = NormalDist().cdf(f1)+(1-NormalDist().cdf(f2))
print('6 = ', Pf)

# 7
g1 = z_value(150)
g2 = z_value(198)
Pg = NormalDist().cdf(g1)+(1-NormalDist().cdf(g2))
print('7 = ', Pg)

# 8
i = z_value(166)
Pi = NormalDist().cdf(i)
print('8 = ', Pi)
