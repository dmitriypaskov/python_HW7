import string
import keyword
"""Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
Змінна не може:
    -починатися з цифри.
    -складатися тільки з цифр.
    -містити великі літери, пропуск і знаки пунктуації (взяти можна тут string.punctuation)
     окрім нижнього підкреслення "_".
    -бути жодним із зареєстрованих слів.
При цьому ім'я змінної може складатися тільки з одного нижнього підкреслення "_".
Список зареєстрованих слів можна взяти із keyword.kwlist.
У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :)) """
value = input("Please enter the name of the variable to check :\n")
result = True
if not value.islower() and value != "_":
    result = False
if value[0].isnumeric() or value.isnumeric():
    result = False
if value in keyword.kwlist:
    result = False
for i, el in enumerate(value):
    if el == " ":
        result = False
        break
    elif len(value) > 1 and value[-i] == "_" and value[-i-1] == "_":
        result = False
        break
    elif el == "_":
        continue
    elif el in string.punctuation:
        result = False
        break


