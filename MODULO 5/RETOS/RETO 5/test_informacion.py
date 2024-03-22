from informacion import * 

ingreso_datos = int(input("Cuantos datos desea ingresar: "))

for i in range(ingreso_datos):
    name = input(f"Ingrese su Nombre y apellido {i+1}: ")
    anio_nacimiento = int(input(f"Ingrese su año de nacimiento {i+1}: "))
    agregar_nombre(name)
    agregar_edad(anio_nacimiento)
mostrar_info()

    