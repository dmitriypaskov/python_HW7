"""Завдання ускладнюється.
Ваша функція is_even, як і раніше, повинна повертати True якщо число парне,
або False якщо число непарне, але при цьому НЕ МОЖНА використовувати ділення у функції,
та дії пов'язані з ним. Тобто. заборонено використовувати /, //, % та divmod
Складність ще полягає і в тому, щоб знайти рішення, яке не залежало б від розміру числа :)
Вхідні дані: Ціле число.
Вихідні дані: True або False"""


def is_even(number: int):
    last = str(number)[-1]
    if int(last) == 1 or int(last) == 3 or int(last) == 5 or int(last) == 7 or int(last) == 9:
        return False
    else:
        return True


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('Ok')
