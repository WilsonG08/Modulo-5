class Auto:
    def __init__(self, marca, modelo, anio, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print("\nInformacion del Automovil:")
        print("Auto 1: ")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")

    def actualizar_kilometraje(self, nuevo_kilometraje):
        if nuevo_kilometraje < self.kilometraje:
            print("\nNo se puede reducir el Kilometraje!!")
        else:
            self.kilometraje = nuevo_kilometraje
    
    def realizar_viajes(self, kilometros_recorridos):
        if kilometros_recorridos > 0:
            self.kilometraje += kilometros_recorridos
        else:
            print(f"La cantidad de Kilometros debe ser positiva! : {kilometros_recorridos}")
        
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo!!")
        elif self.kilometraje >= 20000 and self.kilometraje < 100000:
            print("Ya estoy usado!!")
        elif self.kilometraje > 100000:
            print("!Ya dejame descansar por favor!")



# Instanciando un objeto
auto_Wilson = Auto("Toyota", "Corolla", 2022)
auto_Wilson.mostrar_informacion()
auto_Wilson.actualizar_kilometraje(15000)
auto_Wilson.actualizar_kilometraje(20000)
auto_Wilson.realizar_viajes(5000)
auto_Wilson.realizar_viajes(-100)  
auto_Wilson.estado_auto()
