class Pet:

   def __init__(self, name, species):

       self.name = name

       self.species = species

       self.is_alive = True

       self.age = 0

   def grow(self):

       self.age +=

cat = Pet("Пушок", "кошка")

dog = Pet("Джек", "собака")

cat.grow()

dog.grow()

print(f"{cat.name} растет и ему уже {cat.age} года")

print(f"{dog.name} растет и ему уже {dog.age} года")

