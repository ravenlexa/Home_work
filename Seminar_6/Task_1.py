# Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16.\
# Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95, если выборочная средняя
# M = 80, а объем выборки n = 256.

n = 256
M = 80
sig = 16
Z = 1.96

A = M-Z*sig/n**0.5
B = M+Z*sig/n**0.5
print(f'Доверительный интервал: [{A} ; {B}].')

