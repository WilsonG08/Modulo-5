numero_datos = int(input("Ingrese cuantos datos quiere ingresar: "))

numeros = []
decimal = []
cadenas = []

for i in range(numero_datos):
    dato = input(f"Ingrese el dato {i + 1}: ")
    
    if dato.replace('.', '', 1).isdigit():
        if '.' in dato:
            decimal.append(float(dato))
        else:
            numeros.append(int(dato))
    else:
        cadenas.append(dato)

print(f"\nSu lista de INT ES: {numeros}")
print(f"Su lista de FLOAT ES: {decimal}")
print(f"Su lista de STR ES: {cadenas}")
