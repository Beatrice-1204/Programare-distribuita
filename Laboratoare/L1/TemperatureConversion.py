#1. TemperatureConversion: Scrie un program care cere utilizatorului input grade Celsius si le converteste
#in grade farenheit.
#Farenheit = Celsius x 9/5 + 32

def converiseTemperatura():
    while True:
        try:
            celsius= float(input("Introduceti temperatura in grade Celsius: "))
            break
        except ValueError:
            print("Introduceti temperatura valida")

    fahrenheit = (celsius *9/5)+32
    print(" Fahrenheit: ", fahrenheit)

converiseTemperatura()


#def ruleaza_conversie_temperatura():
 #   celsius = float(input("Introdu temperatura în Celsius: "))
  #  fahrenheit = (celsius * 9 / 5) + 32
   # print(f"Rezultat: {fahrenheit} grade Fahrenheit.")

#ruleaza_conversie_temperatura()


