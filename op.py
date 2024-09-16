class Person:
    def set(self, name, age):
        self.name=name
        self.age=age

    def output(self):
        print(self.name, self.age)

'''p=Person()
p.set("Peter", 20)
p.output()

d=Person()
d.set("Jan", 37)
d.output()

a=input("Ievadiet vārdu: ")
b=int(input("Ievadiet vecumu: "))
c=Person()
c.set(a, b)
c.output()'''

p=Person()
sk=int(input("Ievadiet cilveku skaitu: "))
for i in range(sk):
    a=input("Ievadiet vārdu: ")
    b=int(input("Ievadiet vecumu: "))
    c=Person()
    c.set(a, b)
    c.output()