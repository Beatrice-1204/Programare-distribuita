input_lista = input("Introdu numere separate prin virgula: ")

numere = [int(x.strip()) for x in input_lista.split(",")]



maxim = max(numere)
minim = min(numere)

print(f"Maximul din lista este: {maxim}")
print(f"Minimul din lista este: {minim}")
