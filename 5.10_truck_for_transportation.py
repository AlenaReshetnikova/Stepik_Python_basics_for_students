# Задание № 26
# Задание КИМ № 26: Обработка данных с помощью сортировки
# Раздел № 160: Сортировка данных из файла
#
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3154
#
# Условие задачи:
#
# Для перевозки партии грузов различной массы выделен грузовик, но его грузоподъёмность ограничена, поэтому перевезти
# сразу все грузы не удастся. Грузы массой от 310 до 320 кг грузят в первую очередь, выбирая грузы по убыванию массы,
# начиная с самого тяжёлого. На оставшееся после этого место стараются взять как можно большее количество грузов. Если
# это можно сделать несколькими способами, выбирают тот способ, при котором самый большой из выбранных грузов имеет
# наибольшую массу. Если и при этом условии возможно несколько вариантов, выбирается тот, при котором наибольшую массу
# имеет второй по величине груз, и т.д. Известны количество грузов, масса каждого из них и грузоподъёмность грузовика.
# Необходимо определить количество и общую массу грузов, которые будут вывезены при погрузке по вышеописанным правилам.
#
# Формат входных данных
#
#  Первая строка содержит два числа: N – общее количество грузов и грузоподъëмность грузовика. Каждая из следующих
# N строк содержит массу каждого груза.
#
#
# Формат выходных данных
#
# Два целых числа: сначала максимально возможное количество грузов, затем их общую массу.
#
# Пример входного файла:
#
# 6 720
# 100
# 315
# 120
# 160
# 140
# 300
# В данном случае сначала нужно взять груз массой 315 кг. Остается 405 кг.
#
# После этого можно вывезти ещё максимум
# 3 груза. Это можно сделать тремя способами: 100 + 120 + 140, 100 + 140 + 160, 100 + 120 + 160.
#
# Выбираем способ, при
# котором вывозится груз наибольшей возможной массы. Таких способов два: 100 + 120 + 160, 100 + 140 + 160.
#
# Из этих
# способов выбираем тот, при котором больше масса второго по величине груза, то есть 100 + 140 + 160. Всего получается 4
# груза общей массой 715 кг. Ответ: 4 715.
#
# Примечание
#
# Алгоритм решения данной задачи можно найти на сайте Полякова К.Ю. в разделе ЕГЭ:
# https://kpolyakov.spb.ru/school/ege.htm
#
# Однако навык решения алгоритмических задач формируется в большей степени, если получается решить задачу
# самостоятельно.
#
# Sample Input:
# 6 720
# 100
# 315
# 120
# 160
# 140
# 300
#
# Sample Output:
# 4 715
def get_weights_on_truck(max_weight, items):
    # adding heaviest items with weight between 310 - 320
    items.sort(reverse=True)
    if items == []:
        return 0, 0
    weight_in_truck = 0
    truck = []
    items_left = []
    for i in items:
        if 310 <= i <= 320:
            if weight_in_truck + i <= max_weight:
                truck.append(i)
                weight_in_truck += i
        else:
            items_left.append(i)
    max_weight -= weight_in_truck
    items_left = list(filter(lambda i: i <= max_weight, items_left))
    placement_options = []
    if max_weight < items_left[0]:
        return len(truck), sum(truck)
    if max_weight == items_left[0]:
        return len(truck) + 1, sum(truck) + items_left[0]
    placement_options.append((items_left[0],))
    for item in items_left[1:]:
        new_options = []
        for option in placement_options:
            try_option = (*option, item)
            if sum(try_option) <= max_weight and try_option not in placement_options:
                new_options.append(try_option)
        placement_options += new_options
        if (item,) not in placement_options:
            placement_options.append((item,))
    max_option_len = max(map(len, placement_options))
    max_len_options = list(filter(lambda i: len(i) == max_option_len, placement_options))

    weight = max(map(sum, max_len_options))
    #heavyest_option = sorted([i for i in max_len_options if sum(i) == weight])[::-1][0]
    weight += sum(truck)
    number_of_items = max_option_len + len(truck)

    return number_of_items, weight


# col_items, max_weight_ = map(int, input().split())
# items_ = [int(input()) for i in range(col_items)]

tests = [
    (720, [100, 315, 120, 160, 150, 150, 170, 130, 140, 300]),
    # (800, [310, 320, 315, 319]),
    # (0, []),
    # (947, [312, 317, 315, 310, 320]),
    (316, [310, 1, 2, 2, 3, 3, 4]),
    (310 + 110 + 130 + 150, [310, 110, 130, 150, 120, 160, 300]),
    (310 + 110 + 110 + 130 + 150, [310, 110, 110, 130, 150, 120, 160, 300]),
    (310 + 110 + 110 + 110 + 130 + 150, [310, 110, 110, 110, 150, 120, 130, 160, 300, 125, 155])
]
for test in tests:
    max_weight = test[0]
    items_ = test[1]
    print(f'max_weight: {max_weight}, items: {items_},  result: {get_weights_on_truck(max_weight, items_)}')
