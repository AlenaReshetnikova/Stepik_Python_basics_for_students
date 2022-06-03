# Треугольник Паскаля
# Даны два числа n и m. Создайте массив n × m и заполните его по следующим правилам:
#
# Числа, стоящие в строке 0 или в столбце 0 равны 1.
# Для всех остальных элементов массива A[i][j] = A[i-1][j] + A[i][j-1], то есть каждый элемент равен сумме двух
# элементов, стоящих слева и сверху от него.
# Формат входных данных
#
# Вводятся два натуральных числа n и m (0 < n <= 100; 0 < m <= 100).
#
# Формат выходных данных
#
# Вывести созданный массив на экран.

# Sample Input:
#   5 7
# Sample Output:
#   1 1 1 1 1 1 1
#   1 2 3 4 5 6 7
#   1 3 6 10 15 21 28
#   1 4 10 20 35 56 84
#   1 5 15 35 70 126 210

colich = list(map(int, input().split()))
masi = [list(map(int, "1"*colich[1]))]
print(*list(map(int, "1"*colich[1])))
for i in range(colich[0]-1):
    new_ = [0]
    for j in range(colich[1]):
        new_.append(masi[i][j] + new_[-1])
    masi.append(new_[1:])
    print(*new_[1:])
