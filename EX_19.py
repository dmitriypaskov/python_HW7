"""Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без
урахування знаків пунктуації та регістру букв.
Функція приймає на вхід рядок, та повертає булеве значення True або False"""
import math
import string


def is_palindrome(text):
    letters = "".join(i.lower() for i in text if i not in string.punctuation and not i.isspace())
    return letters == letters[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
