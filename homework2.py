# Я зроблю напевно 2 задачі
# 2
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"{self.make} {self.model} {self.year}"

Car1 = Car("Mazda", "Cx-5 Touring", 2020)
Car2 = Car("Volkswagen", "ID.4 Pro S", 2022)
Car3 = Car("Mazda", "Cx-5 Touring", 2016)
Car4 = Car("Mitsubishi", "L200", 2024)
Car5 = Car("Mitsubishi", "Pajero Sport", 2024)
Car6 = Car("Toyota", "Land Cruiser", 2022)
Car7 = Car("Toyota", "Hilux", 2023)
print(Car1.get_info())
print(Car2.get_info())
print(Car3.get_info())
print(Car4.get_info())
print(Car5.get_info())
print(Car6.get_info())
print(Car7.get_info())
# 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_perimeter(self):
        return 2*self.width+2*self.height
    def calculate_area(self):
        return self.width*self.height
weight=int(input("Введіть ширину"))
height=int(input("Введіть висоту"))
rectangle=Rectangle(weight, height)
print(f"Площа: {rectangle.calculate_area()}")
print(f"Периметр: {rectangle.calculate_perimeter()}")
