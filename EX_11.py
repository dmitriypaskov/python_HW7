"""Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче
Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення
- якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи."""
request_to_user = "y"
while request_to_user == "yes" or request_to_user == "y":
    a = int(input('Please enter first number: '))
    b = int(input('Please enter second number: '))
    act = input('Please enter action: ')
    if act == '+':
        print("You result ", a + b)
    if act == '-':
        print("You result ", a - b)
    if act == '*':
        print("You result ", a * b)
    if act == '/' and b != 0:
        print("You result ", a / b)
    elif act == '/' and b == 0:
        print("You can't divide by 0")
    request_to_user = input("Do you want to perform another calculation? If yes, input 'yes' or 'y'.")
else:
    print("The work is finished. Thank you =)")