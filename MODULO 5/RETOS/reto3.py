print("\n ***  MENU DE SEGUNDA ES TODO! ***\n")
print("OPCIONES")
print("1. Añadir plato al menú.")
print("2. Buscar en el menú.")
print("3. Eliminar plato del menú.")
print("4. Mostrar platos del menú.\n")

menu = ["Ceviche mixto", "Encebollado", "Super Bowl"]

opcion = int(input("Ingrese la opcion: "))


if opcion == 1:
    print("\nAÑADIR PLATO AL MENÚ")
    print(f"\n {menu}\n")
    menu.append(input("Ingrese el plato: "))
    print(f"\nEl menu despues de ser modificado: \n {menu}\n")
elif opcion == 2:
    print("\n BUSCAR EN EL MENÚ")
    buscar_plato = input("Ingrese el plato a buscar en el menu: ")
    if buscar_plato in menu:
        print(f"Plato encontrado: {buscar_plato}")
    else:
        print(f"No se ha encontrado el plato {buscar_plato}")
elif opcion == 3:
    print("\n ELIMINAR PLATO \n")
    print(f"\n {menu} \n")
    plato_eliminar = input("Ingrese el palto a eliminar: ")
    if plato_eliminar in menu:
        menu.remove(plato_eliminar)
        print(f"\n El plato {plato_eliminar} ha sido eliminado con exito!! ")
        print(f"\n {menu} \n")
    else:
        print(f"\n No existe el plato: {plato_eliminar}!!")
elif opcion == 4:
    print("\n MOSTRAR PLATOS DEL MENÚ \n")
    print(menu)
else:
    print(f"\nNo existe la opcion que ingreso: {opcion}!!")
    

