class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Person created")


    def say_hello(self):
        print(f'{self.name} says hello!')


class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
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


p1=Grade("Tom", 15)
t1=Teacher("Katy", 25)
p1.say_hello()
t1.say_hello()
p1.study()
t1.teach()
p1.olympic()