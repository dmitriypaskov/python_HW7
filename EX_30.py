from EX_28 import Student


class StudentClone(Student):

    def __init__(self, gender: str, age: str, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name, record_book)


st1 = StudentClone('Male', 30, 'Steve', 'Jobs', 'AN142')
print(st1)
