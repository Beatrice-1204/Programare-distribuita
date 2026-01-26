input_lista = input("Introdu numere separate prin virgula: ")

numere = [int(x.strip()) for x in input_lista.split(",")]

lista_unica = []
for n in numere:
    if n not in lista_unica:
        lista_unica.append(n)

print("Lista fara duplicate:")
print(", ".join(str(x) for x in lista_unica))
