#GradingSystem: Scrie un program care cere utilizatorului să introducă un scor procentual
#(0-100). Pe baza scorului, programul va afișa nota corespunzătoare utilizând următoarele
#criterii:
#90 și peste: Nota A
#80 până la 89: Nota B
#70 până la 79: Nota C
#60 până la 69: Nota D
#Sub 60: Nota F

def grading_system():
    while True:
        try:
            scor=int(input("Introduceti un numar inre 0-100 "))
            if 0<= scor <= 100:
                break
            print("Eroare. Scorul trebuie sa fie intre 0 si 100")
        except ValueError:
            print("Eroare. Introduceti un numar intreg valid ")


    if scor >=90:
        print(" Nota A")
    elif scor >=80:
        print("Nota B")
    elif scor >=70:
        print("Nota C")
    elif scor >=60:
        print("Nota D")
    elif scor <60:
        print("Nota F")
grading_system()





#score = int(input("Introdu scorul (0-100): "))
#if score >= 90:
 #   print("Nota A")
#elif score >= 80:
 #   print("Nota B")
#elif score >= 70:
 #   print("Nota C")
#elif score >= 60:
 #   print("Nota D")
#else:
#    print("Nota F")
