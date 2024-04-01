import random

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
    
    # Sobreescritura
    def realizar_diagnostico_sistema(self):
        resultado = {
            "MARCA": f"{self.marca}",
            "PROCESADOR ": f"{self.procesador}",
            "MEMORIA RAM" : "OK" if self.memoria >= 8 else "Aumentar memoria RAM",
            "BATERIA " : "OK" if random.choice([True, False]) else "Cambiar de bateria"
        }
        return resultado
    
    # Metodos estaticos
    @staticmethod
    def comparar_costo(laptop1, laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los costos son iguales!"
        return "Los costos son diferentes!"
    
    # Metodo de clase!
    @classmethod
    # CLS referencia a la clase
    def asus_laptop(cls, costo):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        # Te fijas en el metodo constructor
        return cls(marca, procesador, memoria, costo)
    
    