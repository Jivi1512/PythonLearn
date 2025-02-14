class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def key(self):
        return f"{self.name} is {self.age} years old"

class child(person):
    def __init__(self, name, age):
        person.__init__(self,name,age)
p=child("John",36)
print(p.name)
print(p.age)
print(p.key)
