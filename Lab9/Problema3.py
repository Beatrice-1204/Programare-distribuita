import math


class Shape:
    def area(self):
        raise NotImplementedError("Metoda area() trebuie implementată în subclase.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius:g} has area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def area(self):
        return self.width * self.height

    def __str__(self):
        # aria dreptunghiului e de obicei număr “curat”, dar o afișăm robust
        return f"Rectangle with width {self.width:g} and height {self.height:g} has area {self.area():g}"


# Exemplu de utilizare (fără valori prestabilite)
r = float(input("Raza cercului: "))
circle = Circle(r)

w = float(input("Lățime dreptunghi: "))
h = float(input("Înălțime dreptunghi: "))
rectangle = Rectangle(w, h)

print(circle)
print(rectangle)

# Polymorphism: aceeași interfață (area) pentru tipuri diferite
shapes = [circle, rectangle]
print("\nArii calculate polimorfic:")
for s in shapes:
    print(type(s).__name__, "->", s.area())
