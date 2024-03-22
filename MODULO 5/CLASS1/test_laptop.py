from laptop import Laptop

# Creacion de objetos
laptop_prepito = Laptop("Lenovo", "17", 32)
laptop_maria = Laptop("Lenovo", "17", 600)


# Nuevo objeto 
# asus_laptop = Laptop.asus_laptop()
# print(asus_laptop.__dict__)

for numero in range(1, 1000):
    asus_laptop = Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)




#print(Laptop.comparar_costo(laptop_maria, laptop_prepito))