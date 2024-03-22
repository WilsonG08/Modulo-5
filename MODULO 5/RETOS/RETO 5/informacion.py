nombre_paciente = []

def agregar_nombre(nombre):
    nombre_paciente.append(nombre)

edad = []

def agregar_edad(anio_nacimiento):
    anio_actual = 2024
    edad_final = anio_actual - anio_nacimiento
    edad.append(edad_final)

def mostrar_info():
    indicePacienteMayor = edad.index(max(edad))
    indicePacienteMenor = edad.index(min(edad))
    print(f"El paciente mas adulto es: {nombre_paciente[indicePacienteMayor]} con {max(edad)} años")
    print(f"El paciente mas joven es: {nombre_paciente[indicePacienteMenor]} con {min(edad)} años")

    print(nombre_paciente)
    print(edad)


