# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
p1 = 0.1
p2 = 0.2
p3 = 0.25
q1 = 1 - p1
q2 = 1 - p2
q3 = 1 - p3

# Вероятность выхода из строя всех деталей
A = p1 * p2 * p3
print('Вероятность выхода из строя всех деталей: ', A)

# Вероятность выхода из строя только двух деталей
A1 = p1 * p2 * q3  # выйдет из строя 1 элемент и 2, а 3 будет работать
A2 = p1 * q2 * p3  # выйдет из строя 1 элемент и 3, а 2 будет работать
A3 = q1 * p2 * p3  # выйдет из строя 2 элемент и 3, а 1 будет работать
Ab = A1 + A2 + A3
print('Вероятность выхода из строя только двух деталей: ', Ab)

# Вероятность выхода хотя бы 1 детали
Ar = q1 * q2 * q3  # Вероятность выхода из строя всех деталей
Av = 1 - Ar
print('Вероятность выхода хотя бы 1 детали: ', Av)

# Вероятность выхода из строя от одной до двух деталей
# Ищем по схеме сверху, но теперь для выхода из строя только одной детали
B1 = p1 * q2 * q3
B2 = q1 * p2 * q3
B3 = q1 * q2 * p3
Ag = B1 + B2 + B3 + Ab  # добавляем вероятность выхода из строя 2 деталей
print('Вероятность выхода из строя от одной до двух деталей: ', Ag)
