"""  Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
яка повертатиме всі символи між ними включно.
Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
Приклад:
"a-c" -> abc
"a-a" -> a
"s-H" -> stuvwxyzABCDEFGH
"a-A" -> abcdefghijklmnopqrstuvwxyzA  """
import string
interval = input("Please enter two letters separated by a hyphen :\n")
section = string.ascii_letters[string.ascii_letters.index(interval[0]):string.ascii_letters.index(interval[2]) + 1]
print(section)
