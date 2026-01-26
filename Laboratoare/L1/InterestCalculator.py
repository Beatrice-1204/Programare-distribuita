#Scrie un program ce calculeaza dobanda. Programul va cere utilizatorului
#principalul, rata anuala a dobanzii (ex 5, 6, 10) si timpul in ani.
#Formula: Interest = (Principal x Rate x Time)/100

def calculeaza_dobanda():
    print(" Calculator Dobândă")
    principal = float(input("Principal: "))
    rata = float(input("Rata anuală: "))
    timp = float(input("Timp (ani): "))

    dobanda = (principal * rata * timp) / 100

    print(f"Dobânda totală este: {dobanda}")

calculeaza_dobanda()