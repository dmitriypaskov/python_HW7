import string
import keyword
"""Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
Змінна не може:
    -починатися з цифри.
    -складатися тільки з цифр.
    -містити великі літери, пропуск і знаки пунктуації (взяти можна тут string.punctuation)
     окрім нижнього підкреслення "_".
    -бути жодним із зареєстрованих слів."""
value = input("Please enter the name of the variable to check :\n")
result = True
if not value.islower() and value != "_":
    result = False
elif value[0].isnumeric() or value.isnumeric():
    result = False
elif value in keyword.kwlist:
    result = False
else:
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


