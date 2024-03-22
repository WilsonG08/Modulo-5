class Laptop:
    # Metodo constructor
    def __init__(self, marca, procesador, memoria, costo = 500, impuesto = 10):
        # Creacion de los atributos
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto
    

    def valor_final(self):
        # Con self modificas los valores
        return self.costo + self.impuesto

    def valor_descuento(self, descuento):
        return (self.costo * descuento)/100



# Creacion de objetos
laptop_prepito = Laptop("Lenovo", "17", 32)
print(laptop_prepito.__dict__)
print(laptop_prepito.valor_final())
print(f"El valor desucuento : {laptop_prepito.valor_descuento(10)}")