#NumberGuessing: Creează un joc simplu de ghicit un număr, unde programul alege un
#număr aleator între 1 și 20. Utilizatorul are 5 încercări pentru a ghici numărul. După fiecare
#încercare, programul va oferi feedback ("Prea mare", "Prea mic", sau "Corect!"

import random

numar_secret = random.randint(1, 20)
incercari = 5

for i in range(incercari):
    ghicire = int(input(f"Încercarea {i + 1}/{incercari}. Ghicește numărul: "))

    if ghicire > numar_secret:
        print("Prea mare")
    elif ghicire < numar_secret:
        print("Prea mic")
    else:
        print("Corect! Ai ghicit numărul.")
        break
else:
    print(f"Ai rămas fără încercări. Numărul era {numar_secret}.")
