def encontrar_palabra(frase):
    if "feliz" in frase:
        print("El emoji que te representa es: \U0001F600")
    elif "triste" in frase:
        print("El emoji que te representa es: \U0001F641")

lista = []

def agregar_frase(frase):
    lista.append(frase)
    print(f"La frase fue guardad correctamente: {lista}")

