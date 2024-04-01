from Auto import Auto

# INFORMACION
print("INFORMACION!")
# Instanciar los autos
auto_Gis = Auto("Chevrolet", "SAIL",2015,40000)
auto_Wilo = Auto("Mercedes", "Loco",2021,50000)

auto_Gis.mostrar_informacion()
auto_Wilo.mostrar_informacion()


# Comparar Kilometrajes
print(Auto.comparar_autos(auto_Gis, auto_Wilo))

# Validar año
print(f"El auto de marca: {auto_Gis.marca}",  Auto.validarAnio(auto_Gis.anio))
print(f"El auto de marca: {auto_Wilo.marca}",  Auto.validarAnio(auto_Gis.anio))

# Toyota
auto_Alex = Auto.toyota_auto(30000)
print(auto_Alex.__dict__)

# Auto Antiguo
autoAntiguo = Auto.autoAntiguo("Lambo", "Supra")
autoAntiguo.mostrar_informacion


# # Instanciando un objeto
# auto_Wilson = Auto("Toyota", "Corolla", 2022)
# auto_Wilson.mostrar_informacion()
# auto_Wilson.actualizar_kilometraje(15000)
# auto_Wilson.actualizar_kilometraje(20000)
# auto_Wilson.realizar_viajes(5000)
# auto_Wilson.realizar_viajes(-100)  
# auto_Wilson.estado_auto()