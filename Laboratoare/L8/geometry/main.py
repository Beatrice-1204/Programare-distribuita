from circle import area as circle_area, circumference
from rectangle import area as rectangle_area, perimeter

print("Alege figura geometrică:")
print("1 - Cerc")
print("2 - Dreptunghi")

option = input("Opțiunea aleasă: ")

if option == "1":
    radius = float(input("Introduceți raza cercului: "))
    print("Aria cercului:", circle_area(radius))
    print("Circumferința cercului:", circumference(radius))

elif option == "2":
    length = float(input("Introduceți lungimea dreptunghiului: "))
    width = float(input("Introduceți lățimea dreptunghiului: "))
    print("Aria dreptunghiului:", rectangle_area(length, width))
    print("Perimetrul dreptunghiului:", perimeter(length, width))

else:
    print("Opțiune invalidă.")
