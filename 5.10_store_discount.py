# Задание № 26
# Задание КИМ № 26: Обработка данных с помощью сортировки
# Раздел № 160: Сортировка данных из файла
#
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=2650
#
# Условие задачи:
#
# Магазин предоставляет оптовому покупателю скидку по следующим правилам:
# − на каждый второй товар ценой больше 200 рублей предоставляется скидка 30%;
# − общая цена покупки со скидкой округляется вверх до целого числа рублей;
# − порядок товаров в списке определяет магазин и делает это так, чтобы общая сумма скидки была наименьшей.
# Вам необходимо определить общую цену закупки с учётом скидки и цену самого дорогого товара, на который будет
# предоставлена скидка.
#
# Формат входных данных
#
#  Первая строка содержит число N – общее количество купленных товаров. Каждая из следующих N строк содержит одно
#  целое число – цену товара в рублях.
#
#
# Формат выходных данных
#
# В ответе запишите два целых числа: сначала общую цену покупки с учётом скидки, затем цену самого дорогого товара,
# на который предоставлена скидка.
#
# Пример входного файла
#
# 7
# 225
# 160
# 380
# 95
# 192
# 310
# 60
# В данном случае товары с ценой 60, 95, 160 и 192 не участвуют в определении скидки, остальные товары магазину выгодно
# расположить в таком порядке цен: 380, 225, 310. Скидка предоставляется на товар ценой 225. Его цена со скидкой
# составит 157,5 руб., после округления – 158 руб. Общая цена покупки составит: 60 + 95 + 160 + 192 + 158 + 380 + 310
# = 1355 руб. Самый дорогой товар, на который будет получена скидка, стоит 225 руб. В ответе нужно записать числа 1355
# и 225.
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
# 7
# 225
# 160
# 380
# 95
# 192
# 310
# 60
#
# Sample Output:
# 1355 225
#
# col_box = int(input())
# items = [int(input()) for i in range(col_box)]
import math


def find_total_payment(items_to_pay):
    if len(items_to_pay) == 0:
        return 0, 0
    elif len(items_to_pay) == 1:
        return items_to_pay[0], 0
    expensive_items = sorted([i for i in items_to_pay if i > 200])
    #print(f'expensive_items: {expensive_items}')

    total_payment = sum([i for i in items_to_pay if i <= 200])
    #print(f'sum inexpensive: {[i for i in items_to_pay if i <= 200]}, sum: {total_payment}')

    discounted_items = expensive_items[0:len(expensive_items) // 2]
    #print(f'discouted_items: {expensive_items[0:len(expensive_items) // 2]}')

    total_payment += sum([i for i in expensive_items[len(expensive_items) // 2:]])
    #print(f'total payments: {[i for i in expensive_items[len(expensive_items) // 2:]]}, sum: {total_payment}')

    if discounted_items != []:
        big_discounted_items = discounted_items[-1]
    else:
        big_discounted_items = 0
    sum_discounted_items = sum(discounted_items)
    total_payment += math.ceil(sum_discounted_items - (sum_discounted_items / 100 * 30))
    return total_payment, big_discounted_items


# col_box = 7
tests = [
    [225, 160, 380, 95, 192, 310, 60],
    [220],
    [50],
    [202, 50],
    [202, 50, 202],
    [50, 202, 50],
    [200],
    [200, 200],
    [200, 200, 200],
    [210, 210],
    [210, 210, 210],
    [201, 201, 201],
    []
]
for test in tests:
    print()
    print(test)
    print(*find_total_payment(test))

# print(int(2.1))
