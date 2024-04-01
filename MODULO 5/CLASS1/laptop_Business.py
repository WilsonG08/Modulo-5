from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, tarjeta_graf, almacenamiento, duracion_bateria ,costo=500, impuesto=10):
        # Super para acceder a el metodo de la clase padre
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    # EL mismo nombre porque es hijo
    def realizar_diagnostico_sistema(self):
        # ME devuelve un valor y lo almaceno
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["Almacenamiento"] = f"{self.almacenamiento} GB"
        resultado_diagnostico["Duracion Bateria"] = f"{self.duracion_bateria} horas"
        resultado_diagnostico["Conectividad de Red"] = resultado_conectividad
        return resultado_diagnostico

    def verificar_conectividad_red(self):
       conectvidad = {
           "Wifi": random.choice([True, False]),
           "Acceso a Servidores Empresariales" : random.choice([True, False]),
           "Latencia de Red" : random.randint(1, 100)
       }
       return conectvidad

    pass