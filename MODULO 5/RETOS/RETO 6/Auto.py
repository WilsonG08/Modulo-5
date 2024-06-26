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

    # Metodo estatico 
    @staticmethod
    def comparar_autos(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        return "Tienen diferente "
    
    @classmethod
    def toyota_auto(cls, kilometraje):
         marca= "Toyota"
         modelo= "Sail"
         año= "2024"
         return cls(marca,modelo,año,kilometraje)
    
    @classmethod
    def autoAntiguo(cls, marca, modelo):
        return cls(marca, modelo, 1990)
    
    @staticmethod
    def validarAnio(anio):
        if anio >= 2000 and anio <= 2024:
            return "Es un auto de la decada de los 2000"
        else:
            return "Es un auto de la decada de los 90"
    