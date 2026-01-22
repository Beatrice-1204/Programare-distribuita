import math

# Citirea datelor de la utilizator
num = int(input("Introduceți un număr întreg: "))
angle = float(input("Introduceți un unghi în grade: "))

# 1. Rădăcina pătrată
sqrt_value = math.sqrt(num)

# 2. Factorial
factorial_value = math.factorial(num)

# 3. Sinusul unghiului (conversie din grade în radiani)
sin_value = math.sin(math.radians(angle))

# Afișarea rezultatelor
print(f"Rădăcina pătrată a {num} este {sqrt_value}")
print(f"Factorialul lui {num} este {factorial_value}")
print(f"Sinusul unghiului de {angle} grade este {sin_value}")
