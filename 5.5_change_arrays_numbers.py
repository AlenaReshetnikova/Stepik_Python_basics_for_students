# Дан двумерный массив размером  n × m и два числа: i и j. Поменяйте в массиве столбцы с индексами i и j
#
# Формат входных данных
#
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой (0 < n <= 100; 0 < m <= 100),
# затем числа i и j.
#
# Формат выходных данных
#
# Выведите результат.
# Sample Input 1:
#
# 3 4
# 1 3 2 4
# 2 3 5 5
# 5 1 2 4
# 0 3
# Sample Output 1:
#
# 4 3 2 1
# 5 3 5 2
# 4 1 2 5
# Sample Input 2:
#
# 2 2
# 0 1
# 1 0
# 0 1
# Sample Output 2:
#
# 1 0
# 0 1
colich = list(map(int, input().split()))
mas = []
for i in range(colich[0]):
    mas.append(list(map(int, input().split())))
cha = list(map(int, input().split()))
for i in mas:
    will = i[cha[0]]
    i[cha[0]] = i[cha[1]]
    i[cha[1]] = will
    print(*i)
