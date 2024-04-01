from laptop import Laptop
from laptop_gaming import Laptop_gaming
from laptop_Business import Laptop_Business

# Creacion de objetos
laptop_prepito = Laptop("Lenovo", "17", 32)
laptop_maria = Laptop("Lenovo", "17", 32, 600)


# Nuevo objeto 
# asus_laptop = Laptop.asus_laptop()
# print(asus_laptop.__dict__)

# for numero in range(1, 1000):
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)

#print(Laptop.comparar_costo(laptop_maria, laptop_prepito))
    
# Nuevo objeto
lapto_juanito = Laptop_gaming("MSI", "i7", 4, "RTX 8GB")
# print(lapto_juanito.realizar_diagnostico_sistema())

# lapto_empresa = Laptop_Business("HP", "I7", 16, 521, 8, 85)
# print(lapto_empresa.realizar_diagnostico_sistema())

# CREACION DE LA FUNCION PARA IMPRIMIR LA INFO
def imprimir_infome(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave}: {valor}")
    print("\n")


print("PEPITO: ")
imprimir_infome(laptop_prepito)

print("JUANITO: ")
imprimir_infome(lapto_juanito)

