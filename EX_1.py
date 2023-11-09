'''Написати програму, яка переміщає всі нулі у кінець списку.
Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
Порядок ненульових чисел має зберегтися!'''
arr = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
numbers = []
zeros = []
res = []
i = 0
while i < len(arr):
    if arr[i] != 0:
        numbers.append(arr[i])
    else:
        zeros.append(arr[i])
    i += 1
res.extend(numbers)
res.extend(zeros)
print(res)
