pais = input("Ingrese el país Colombia, Ecuador, o Peru?: ")
zona = input("Ingrese la zona urbana, rural, perimetral?: ")
velocidadStr = input("Ingrese la velocidad actual del conductor en Km/h: ")
velocidad = int(velocidadStr)

if pais == "Ecuador":
    if zona == "urbana":
        if 10 <= velocidad <= 50:
            print("El conductor respeta los límites de velocidad.")
        else:
            print("El conductor no respeta los límites de velocidad.")
    elif zona == "rural":
        if 51 <= velocidad <= 70:
            print("El conductor respeta los límites de velocidad.")
        else:
            print("El conductor no respeta los límites de velocidad.")
    elif zona == "perimetral":
        if 71 <= velocidad <= 90:
            print("El conductor respeta los límites de velocidad.")
        else:
            print("El conductor no respeta los límites de velocidad.")
    else:
        print("Zona no válida.")
else:
    print("País no válido.")
