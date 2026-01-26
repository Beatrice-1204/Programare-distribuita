#Creeaza un program care cere userului un numar intreg si afiseaza daca acest numar este
#par sau impar. (hint, '%' returneaza restul impartirii)

def OddOrEven():
    while True:
        try:
            numar=int(input("Introduceti un numar "))
            break
        except ValueError:
            print("Introduceti un numar intreg")
    if numar%2==0:
        print("Numarul este par")
    else:
        print("numarul este impar")

OddOrEven()



#def verifica_par_sau_impar():
 #   numar = int(input("Introdu un număr întreg: "))

  #  if numar % 2 == 0:
   #     print(f"Numărul {numar} este par.")
    #else:
     #   print(f"Numărul {numar} este impar.")

#verifica_par_sau_impar()