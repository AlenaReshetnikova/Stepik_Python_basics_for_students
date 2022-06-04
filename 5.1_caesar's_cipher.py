# Шифр Цезаря
# В шифре Цезаря каждый символ заменяется на другой символ, третий по счету в алфавите после данного, с цикличностью.
# То есть символ A заменяется на D, символ B - на E, символ C - на F, ..., символ Z на C. Аналогично строчные буквы
# заменяются на строчные буквы. Все остальные символы не меняются.
#
# Тем, кому интересны темы связанные с шифрами, рекомендую уроки и видео:
#
# https://ru.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher Уроки от Академии Хана на
# русском: Криптография/ Древняя криптография/ Шифр Цезаря.
# http://mmmf.msu.ru/circles/z4_Podgaits/03.html МАЛЫЙ МЕХМАТ МГУ; Кружок 4 класса; Криптография
# Для написания алгоритма следует осознать математическую модель (https://ru.wikipedia.org/wiki/Шифр_Цезаря)
#
#
#
# Уточнение (математической модели из Wiki):
#
# # если представить данное математическое выражение на языке Python
#
# y = (x + k) % n
#
# # Нумерация символов в алфавите начинается с нуля.
# # y - порядковый номер символа в алфавите, которым шифруется исходный символ
# # x - порядковый номер исходного (подлежащего шифрованию) символа
# # k - ключ (shift) число, указывающее на сколько символов нужно осуществить сдвиг вправо
# # (в данной конкретной задаче это цикличный сдиг вправо на 3 символа)
# # n - количество символов в алфавите (мощность алфавита)
# # n = 26 (для английского алфавита)
# Условие задачи
# Дана строка на английском языке, зашифруйте ее при помощи шифра Цезаря.
#
# Каждый символ заменяется на другой символ, третий по счету в алфавите после данного, с цикличностью (например,
# символ "y" заменяется на "b"). То есть символ A заменяется на D, символ B - на E,... Аналогично строчные буквы
# заменяются на строчные буквы. Все остальные символы не меняются.
#
# Формат входных данных
#
# Символьная строка (в данной задаче шифруются только символы английского алфавита).
# Формат выходных данных
#
# Зашифрованная символьная строка.
#
# Подсказка
#
# Прописные буквы шифруются так, как показано в Sample Input 2, Sample Output 2 (аналогичным образом шифруются
# строчные).
#
# Sample Input 1:
# Everybody has won, and all must have prizes.
#
# Sample Output 1:
# Hyhubergb kdv zrq, dqg doo pxvw kdyh sulchv.
#
# Sample Input 2:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#
# Sample Output 2:
# D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
#
# Sample Input 3:
# abc 123 абвгд ABCD #$%^
#
# Sample Output 3:
# def 123 абвгд DEFG #$%^

import string


def find_sim(sim_in, alfab):
    shift_ = 3
    col_num = 26
    sim_in = alfab.index(sim_in)
    new_index = (sim_in + shift_) % col_num
    return alfab[new_index]

alfabet = string.ascii_lowercase
alfabet_uppercase = string.ascii_uppercase
str_ = list(input())
new_str = []
for i in range(len(str_)):
    if str_[i] in alfabet:
        new_str.append(find_sim(str_[i], alfabet))
    elif str_[i] in alfabet_uppercase:
        new_str.append(find_sim(str_[i], alfabet_uppercase))
    else:
        new_str.append(str_[i])
print(''.join(new_str))
