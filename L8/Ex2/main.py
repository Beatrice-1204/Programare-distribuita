import math_operations

# Citirea datelor de la utilizator
a = float(input("Introduceți primul număr: "))
b = float(input("Introduceți al doilea număr: "))

# Alegerea operației
print("Alegeți operația:")
print("1 - Adunare")
print("2 - Scădere")
print("3 - Înmulțire")
print("4 - Împărțire")

option = input("Opțiunea aleasă: ")

# Executarea operației
if option == "1":
    print("Rezultat:", math_operations.add(a, b))
elif option == "2":
    print("Rezultat:", math_operations.subtract(a, b))
elif option == "3":
    print("Rezultat:", math_operations.multiply(a, b))
elif option == "4":
    print("Rezultat:", math_operations.divide(a, b))
else:
    print("Opțiune invalidă.")
