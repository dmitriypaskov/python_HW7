import random
""" Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця. """
arr = [random.randint(0, 100) for i in range(random.randint(3, 10))]
res = [arr[0], arr[2], arr[-2]]
print(len(arr))
print(arr)
print(res)
