# Agregar elementos a una lista

lista = [1,2,3,4,5]
# Agrega al final
lista.append(6)

# Recibe dos parametros, el uno es un indice y el otro es valor
lista.insert(2, "Wilson")


# Agregar una lista a otra lista creada, recibe como parametro otra lista
lista.extend([6,7,8,9])
print(lista)

lista2 = [6,7,8,9]
lista3 = lista + lista2

print(lista3)