
#MultiplesFinder: Scrie un program care cere utilizatorului să introducă două numere, x și y,
#și afișează toti multiplii lui x care sunt mai mici decât y.

x = int(input("Introdu valoarea lui x: "))
y = int(input("Introdu valoarea lui y: "))

print(f"Multiplii lui {x} mai mici decât {y} sunt:")

for i in range(x, y, x):
    print(i)
