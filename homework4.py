# Я обрала завдання 1 :)
class Animal:
    def __init__(self, breed, color, weight):
        self.breed = breed
        self.color = color
        self.weight = weight

class Cat(Animal):
    def __init__(self, breed, color, weight):
        super().__init__(breed,color,weight)

class Dog(Animal):
    def __init__(self, breed, color, weight):
        super().__init__(breed,color,weight)

class Fish(Animal): # Мені стало нудно і я додала ще тваринку :)
    def __init__(self, breed, color, weight):
        super().__init__(breed,color, weight)

animals = [
    Cat("Bengal", "Golden", 5),
    Dog("Bichon", "White", 6),
    Fish("Ancistrus", "Golden", "0.02")
]
typeOfAnimal = ["Cat", "Dog", "Fish"]
i=0
for animal in animals:
    print(f"{typeOfAnimal[i]} - Breed: {animal.breed}, Color: {animal.color}, Weight: {animal.weight}")
    i += 1