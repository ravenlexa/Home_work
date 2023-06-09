# 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.
p1 = 0.9
p2 = 0.8
p3 = 0.6

A = 1/3 * p1 + 1/3 * p2 + 1/3 * p3

# вероятность того, что выстрел произведен первым спортсменом

b1 = 1/3 * p1 / A
print('Вероятность того, что выстрел произведен первым спортсменом: ', b1)

b2 = 1/3 * p2 / A
print('Вероятность того, что выстрел произведен вторым спортсменом: ', b2)

b3 = 1/3 * p3 / A
print('Вероятность того, что выстрел произведен третьим спортсменом: ', b3)
