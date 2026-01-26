input_tuple = input("Introdu valori separate prin virgula: ")

tupla = tuple(int(x.strip()) for x in input_tuple.split(","))

valoare_cautata = int(input("Cauta valoarea: "))

if valoare_cautata in tupla:
    index = tupla.index(valoare_cautata)
    print(f"{valoare_cautata} se regaseste in tupla la indexul {index}.")
else:
    print(f"{valoare_cautata} nu se regaseste in tupla.")
