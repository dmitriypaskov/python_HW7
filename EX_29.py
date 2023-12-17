"""Створити клас цифрового лічильника. У класі реалізувати методи:
    встановлення максимального значення лічильника,
    встановлення мінімального значення лічильника
    встановлення початкового значення лічильника
    метод step_up збільшує лічильник на 1. Метод можна викликати до тих пір, поки значення досягне максимуму.
При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимуму
    метод step_down зменшує лічильник на 1. Метод можна викликати до тих пір, поки значення не досягне мінімуму.
При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що досягнутий мінімум
    повернення поточного значення лічильника
Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод ініціалізації екземпляра клас
Приблизний каркас для класу та варіанти перевірки. Вам потрібно дописати необхідне замість pass"""


class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int):
        self.current = start

    def set_max(self, max_max: int):
        self.max_value = max_max

    def set_min(self, min_min: int):
        self.min_value = min_min

    def step_up(self):
        try:
            if self.current < self.max_value:
                self.current += 1
            else:
                raise ValueError
        except ValueError:
            print("Досягнено максимуму!")

    def step_down(self):
        try:
            if self.current > self.min_value:
                self.current -= 1
            else:
                raise ValueError
        except ValueError:
            print("Досягнено мінімуму!")

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Досягнено максимуму!
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Досягнено мінімуму!
assert counter.get_current() == 7, 'Test4'
print("Ok")
