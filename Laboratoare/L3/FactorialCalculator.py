def factorial(n):
    rezultat = 1
    for i in range(1, n + 1):
        rezultat *= i
    return rezultat


numar = int(input("Introdu un numar intreg: "))

print(f"Factorialul lui {numar} este {factorial(numar)}")
