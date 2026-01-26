class BankAccount:
    def __init__(self, initial_balance=0.0):
        # atribut “privat” (convenție Python): nu se accesează direct din exterior
        self._balance = float(initial_balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Eroare: suma depusă trebuie să fie pozitivă.")
            return
        self._balance += amount
        print(f"Depunere reușită. Sold nou: {self._balance:.2f}")

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Eroare: suma retrasă trebuie să fie pozitivă.")
            return
        if amount > self._balance:
            print("Eroare: fonduri insuficiente.")
            return
        self._balance -= amount
        print(f"Retragere reușită. Sold nou: {self._balance:.2f}")

    def get_balance(self):
        return self._balance


# Exemplu de utilizare (fără valori prestabilite)
account = BankAccount(float(input("Sold inițial: ")))
while True:
    print("\n1 - Depunere\n2 - Retragere\n3 - Afișează sold\n4 - Ieșire")
    option = input("Alege opțiunea: ")

    if option == "1":
        amount = float(input("Suma pentru depunere: "))
        account.deposit(amount)
    elif option == "2":
        amount = float(input("Suma pentru retragere: "))
        account.withdraw(amount)
    elif option == "3":
        print(f"Sold curent: {account.get_balance():.2f}")
    elif option == "4":
        print("La revedere!")
        break
    else:
        print("Opțiune invalidă.")
