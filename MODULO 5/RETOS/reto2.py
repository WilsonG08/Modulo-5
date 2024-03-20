print("\n ********** [ Kraketravels ] ************\n")
destino = input("¿Cual es su destino? [ Colombia, Ecuador, o Perú ] : ")
limite_velocidad = float(input("Ingrese su velocidad actual [ KM/h ]: "))

if destino == "Ecuador":
    if limite_velocidad >= 10 and  limite_velocidad <= 50:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Urbana!")
    elif limite_velocidad >= 51 and limite_velocidad <=70:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Rural!")
    elif limite_velocidad >= 71 and limite_velocidad <=90:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Perimetral!")
    else:
        print(f"Su velocidad: {limite_velocidad} esat fuera de los rangos!!")
elif destino == "Colombia":
    if limite_velocidad >= 10 and  limite_velocidad <= 30:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Urbana!")
    elif limite_velocidad >= 31 and limite_velocidad <=80:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Rural!")
    elif limite_velocidad >= 81 and limite_velocidad <=100:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Perimetral!")
    else:
        print(f"Su velocidad: {limite_velocidad} esat fuera de los rangos!!")
elif destino == "Peru":
    if limite_velocidad >= 10 and  limite_velocidad <= 40:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Urbana!")
    elif limite_velocidad >= 41 and limite_velocidad <=60:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Rural!")
    elif limite_velocidad >= 61 and limite_velocidad <=120:
        print(f"Usted esta en {destino}, su velocidad es: {limite_velocidad} y esta en Zona Perimetral!")
    else:
        print(f"Su velocidad: {limite_velocidad} esat fuera de los rangos!!")
else:
    print(f"El destino: {destino} no esta en la lista antes mencionada!!!")