"""Напишіть функцію common_elements, яка згенерує два списки елементів .
Один список з числами кратними 3, інший з кратними числами 5. Кількість елементів у цих списках може бути різним.
За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
Функція повинна повернути цю множину як результат своєї роботи.
def common_elements():
    pass"""
import random


def common_elements():
    matrix_3 = set([random.randrange(0, 100, 3) for j in range(random.randrange(3, 20))])
    matrix_5 = set([random.randrange(0, 100, 5) for j in range(random.randrange(3, 20))])
    print(matrix_3)
    print(matrix_5)
    common_set = matrix_3.intersection(matrix_5)
    return common_set


print(common_elements())
