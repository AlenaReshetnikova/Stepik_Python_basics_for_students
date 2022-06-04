# Определите, является ли строка палиндромом (то есть верно ли, что она одинаково читается слева направо и справа
# налево)
#
# Формат входных данных
# На вход подается строка без пробелов. Длина строки не превышает 256. Символы разного регистра считаются различными.
#
# Формат выходных данных
# Необходимо вывести YES, если строка является палиндромом, и NO в противном случае.
#
# Sample Input 1:
# saippuakivikauppias
#
# Sample Output 1:
# YES
#
# Sample Input 2:
# 1234567
#
# Sample Output 2:
# NO
str_ = input()
print("YES" if str_ == str_[::-1] else "NO")
