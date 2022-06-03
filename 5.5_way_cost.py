# Квадрат разлинован на N×N клеток (1 < N < 17). Исполнитель Робот может перемещаться по клеткам, выполняя за одно
# перемещение одну из двух команд: вправо или вниз. По команде вправо Робот перемещается в соседнюю правую клетку,
# по команде вниз – в соседнюю нижнюю. При попытке выхода за границу квадрата Робот разрушается. Перед каждым запуском
# Робота в каждой клетке квадрата лежит монета достоинством от 1 до 100. Посетив клетку, Робот забирает монету с собой;
# это также относится к начальной и конечной клетке маршрута Робота.
#
# Исходные данные записаны в файле 18-10.xls в виде электронной таблице размером N×N, каждая ячейка которой
# соответствует клетке квадрата. Определите максимальную и минимальную денежную сумму, которую может собрать Робот,
# пройдя из левой верхней клетки в правую нижнюю. В ответе укажите два числа – сначала максимальную сумму, затем
# минимальную.
#
# Ответ: 1309 607
#
# Формат входных данных
#
# Исходная таблица:
#  3 4
# 63 78 58 93
# 10 1 42 24
# 25 29 87 76
# Ответ
# 404 216
# В первой строке два числа n строк и m столбцов, далее следуют значения ячеек таблицы.
# Формат выходных данных
#
# Два числа: максимальная сумма и минимальная.

def get_way_cost(min_max, array_, row_, column_):
    new_array = []
    line = [array_[0][0]]
    for b in range(1, column_):
        line.append(array_[0][b] + line[b - 1])
    new_array.append(line)
    for i in range(row_ - 1):
        line = [array_[i + 1][0] + new_array[i][0]]
        for j in range(1, column_):
            line.append(array_[i + 1][j] + min_max(new_array[i][j], line[j - 1]))
        new_array.append(line)
    return line[-1]


row, columns = list(map(int, input().split()))
array = []
for i in range(row):
    array.append(list(map(int, input().split())))

print(get_way_cost(max, array, row, columns), get_way_cost(min, array, row, columns))
