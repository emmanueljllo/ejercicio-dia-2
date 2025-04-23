lista = []

elemento1 = input("ingrese el numero 1: ")
elemento2 = input("ingrese el numero 2: ")
elemento3 = input("ingrese el numero 3: ")

lista.append(elemento1)
lista.append(elemento2)
lista.append(elemento3)


if elemento1 <= elemento2 and elemento1 <= elemento3 :
    print(f"el nunero menor es {elemento1}")

elif elemento2 <= elemento3 and elemento3 <= elemento1:
    print(f"el numero menor es {elemento2}")  

else:
    print(f"el numero menor es {elemento3}")      



