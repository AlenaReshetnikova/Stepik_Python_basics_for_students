# Дан квадратный массив. Поменяйте местами в каждом столбце элементы, стоящие на главной и побочной диагонали.
#
# Формат входных данных
#
# В первой строке дано число n ≤ 10 (размер массива по высоте и ширине).
# Далее идут n строк по n неотрицательных целых чисел не больше 50.
#
# Формат выходных данных
#
# Выведите результат.
# Sample Input:
#
# 5
# 0 0 0 0 0
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# Sample Output:
# 4 0 0 0 4
# 1 3 1 3 1
# 2 2 2 2 2
# 3 1 3 1 3
# 0 4 4 4 0
def change_dioganals(array_):
    array_len = len(array_)
    for i in range(array_len):
        array_[i][i], array_[array_len - 1 - i][i] = array_[array_len - 1 - i][i], array_[i][i]
    for item in array_:
        print(*item)


amount = int(input())
array = []
for i in range(amount):
    array.append(list(map(int, input().split())))
change_dioganals(array)