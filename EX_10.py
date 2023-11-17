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
if value != "_" and not value.islower():
    result = False
elif value[0].isnumeric():
    result = False
elif value in keyword.kwlist:
    result = False
else:
    for el in value:
        if el == "_":
            continue
        elif el == " ":
            result = False
            break
        elif el in string.punctuation:
            result = False
            break


