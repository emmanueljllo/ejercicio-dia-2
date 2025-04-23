def verificar_invitado():
    invitados = ["Ana", "luis", "sofia", "carlos", "elena"]

    nombre = input("por favor, introduce tu nombre: ")

    if nombre.capitalize() in invitados:
        print(f"¡hola {nombre}! estas en la lista de invitados.")
    else:
        print(f"lo siento, {nombre}. no esta en la lista de invitados.")    
verificar_invitado() 