# Общие символы
# Даны два слова. Вывести индексы общих букв двух слов (одинаковых символов, имеющих одинаковый номер вхождения).
# Количество символов в словах может быть произвольной длины. Если слова не содержат общих символов с одинаковыми
# индексами, вывести -1
#
# Формат входных данных
#
# Два слова, каждое с новой строки
#
# Формат выходных данных
#
# Номера индексов, разделенные пробелом
#
# Sample Input 1:
# слово
# словарь
#
# Sample Output 1:
# 0 1 2 3
str_1 = list(input())
str_2 = list(input())
numbers = [i for i in range(min(len(str_2), len(str_1))) if str_1[i] == str_2[i]]
if numbers:
    print(*numbers)
else:
    print(-1)
