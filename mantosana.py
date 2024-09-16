class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Person created")


    def say_hello(self):
        print(f'{self.name} says hello!')


class Student(Person):
    def __init__(self, name, age, average_grade):
        super().__init__(name, age)
        self.average_grade=average_grade
        print("Student created")
    def study(self):
        print(f'{self.name} studies')
    def say_hello(self):
        print(f'Student with name: {self.name} says hello!')

class Grade(Student):
    def olympic(self):
        print(f"{self.name} participates in olympic")


class Teacher(Person):
    def teach(self):
        print(f'{self.name} teaches')


def introduce(person):
    person.say_hello()

people_arr=[Student("Tom", 15, 4.5), Teacher("Katy", 25), Grade("Bob", 26, 4.8)]


for person in people_arr:
    introduce(person)




'''p1=Grade("Tom", 15)
t1=Teacher("Katy", 25)
p1.say_hello()
t1.say_hello()
p1.study()
t1.teach()
p1.olympic()'''