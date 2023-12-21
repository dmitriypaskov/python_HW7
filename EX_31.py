"""У цьому завданні Вам необхідно зробити дві речі на підставі попереднього ДЗ.
До класу Студента необхідно додати метод порівняння.
Порівнювати можна за тими рядками, які повертає метод __str__
Для того, щоб спрацювала коректно ось ця перевірка"""

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

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__str__() == other.__str__()

    def __str__(self):
        return f"{super().__str__()}record_book: {self.record_book}\n\n"


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise TooManyStudentsError()

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


class TooManyStudentsError(Exception):

    def __str__(self):
        return "TooManyStudentsError"


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
gr.delete_student('Taylor')
print(gr)  # Only one student
print(gr.count())
print("Ok")
