#Verificare Număr Prim

import math

def verifNrPrim():
    while True:
        try:
            nr=int(input("Numarul de verificat este:"))
            break
        except ValueError:
            print("Nu ati introdus un numar intreg. Incercati din nou")

    if nr <=1:
        print(f"Numarul {nr} nu este prim")
        return
    elif nr==2:
        print(f"Numarul {nr} este prim")
        return
    elif nr%2==0:
        print(f"Numarul {nr} nu este prim")
        return

    for i in range(3, int(math.isqrt(nr))+1, 2):
        if nr%i==0:
            print(f"Numarul {nr} nu este prim")
            return
    print(f"Numarul {nr} este prim")

verifNrPrim()



#def verifica_prim():
#    numar = int(input("Introdu numărul : "))

#    if numar <= 1:
#        print(f"{numar} NU este prim.")
#        return  # Oprește funcția aici, nu merge mai departe

#    for i in range(2, numar):
#        if numar % i == 0:
#           print(f"{numar} NU este prim .")
#            return
#    print(f"{numar} ESTE un număr prim.")
#verifica_prim()