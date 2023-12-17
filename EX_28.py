"""1) Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
3) Створіть клас Група, екземпляр якого складається з об'єктів класу Студент. Реалізуйте методи додавання,
видалення студента та метод пошуку студента на прізвище.
Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
Визначте для групи метод __str__() для повернення списку студентів у вигляді рядка.
Нижче наведені заготовки, які необхідно доповнити."""

from abc import ABC, abstractmethod


class Human(ABC):

    def __init__(self, gender: str, age: str, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    @abstractmethod
    def __str__(self):
        return f"gender: {self.gender}\nage: {self.age}\nfirst_name: {self.first_name}\nlast_name: {self.last_name}\n"


class Student(Human):

    def __init__(self, gender: str, age: str, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}record_book: {self.record_book}\n\n"


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        try:
            if len(self.group) < 10:
                self.group.add(student)
            else:
                raise ValueError
        except ValueError:
            print("ExceptGroupFull")

    def delete_student(self, last_name: str):
        if self.find_student(last_name) in self.group:
            self.group.remove(self.find_student(last_name))

    def find_student(self, last_name: str):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def count(self):
        return len(self.group)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__()
        return f'Number:{self.number}\n\n{all_students} '


# class ExceptGroupFull:
#
#     def __init__(self, group):
#         self.group = group
#
#     def group_except(self):
#         assert self.group == 10, 'Test1'
#         try:
#             self.group.add_student()
#         except ValueError as ExceptGroupISFull:
#             print(ExceptGroupISFull)
#         assert self.group == 10, 'Test2'


gr = Group('PD1')
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')

for i in range(10):
    gr.add_student(Student('Male', 30, 'Steve', 'Jobs', 'AN142'))
gr.add_student(st1)

print(gr.count())
print("Ok")
