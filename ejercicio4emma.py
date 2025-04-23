def validar_edad():
    try:
        edad = int(input("por favor, introdusce tu edad: "))

        if edad < 0 or edad > 120:
            print("edad no valida")
        else:
            print("edad valida")
    except ValueError:
        print("edad no valida, por favor, introduce un numero.")
validar_edad()                