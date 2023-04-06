class Person:
  x = 5
  y = 6
  def __init__(self,x,y):
    self.x = x;
    self.y = y;
  def add(self):
    return self.x + self.y
person = Person(10, 20)
person.z = 7
print(person.x)
print(person.y)
print(Person.x)
print(Person.y)
print(Person.add(Person))
print(person.add())
print(Person.z)