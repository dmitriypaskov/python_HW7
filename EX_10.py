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
Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
_ => True
x => True
get_value => True
get value => False
get!value => False
some_super_puper_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
m3 => True
НЕ МОЖНА ВИКОРИСТОВУВАТИ RegEx."""
#value = input("Please enter the name of the variable to check :\n")
value = "__ifр"
result = True
#result = False
if value.islower():
    result = True
else:
    result = False
if value[0].isnumeric():
    result = False
else:
    result = True
if not value.isnumeric():
    print("Не складається лише з цифр")
if value not in keyword.kwlist:
    print("Не зарезервоване слово")
for i, el in enumerate(value):
    if el == " ":
        break
    elif value[i] == "_" and value[i+1] == "_":
        break
    elif el == "_":
        continue
    elif el not in string.punctuation:
        print("Не є спецсимволом" + el)
print(result)

