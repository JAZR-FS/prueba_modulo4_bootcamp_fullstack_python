##################################
##           PARTE 1            ##
##################################
print("\nESTAMOS VIENDO LA PARTE 1")


class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje


# Crear tres instancias de prueba para Automovil
automovil1 = Automovil("Toyota", "Yaris", 4, 120, 800)
automovil2 = Automovil("Fiat", "Palio", 4, 95, 1200)
automovil3 = Automovil("Ford", "Fiesta", 4, 125, 1500)

# Mostrar las instancias
print(
    f"Marca: {automovil1.marca}, Modelo: {automovil1.modelo}, Ruedas: {automovil1.nro_ruedas}, Velocidad: {automovil1.velocidad} Km/h, Cilindraje: {automovil1.cilindraje} cc"
)
print(
    f"Marca: {automovil2.marca}, Modelo: {automovil2.modelo}, Ruedas: {automovil2.nro_ruedas}, Velocidad: {automovil2.velocidad} Km/h, Cilindraje: {automovil2.cilindraje} cc"
)
print(
    f"Marca: {automovil3.marca}, Modelo: {automovil3.modelo}, Ruedas: {automovil3.nro_ruedas}, Velocidad: {automovil3.velocidad} Km/h, Cilindraje: {automovil3.cilindraje} cc"
)


##################################
##           PARTE 2            ##
##################################
print("\nESTAMOS VIENDO LA PARTE 2")


class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindraje)
        self.nro_puestos = nro_puestos


class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindraje)
        self.carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios


# Crear instancias de prueba adicionales
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# Mostrar las instancias adicionales
print(
    f"Marca: {particular.marca}, Modelo: {particular.modelo}, Ruedas: {particular.nro_ruedas}, Velocidad: {particular.velocidad} Km/h, Cilindraje: {particular.cilindraje} cc, Puestos: {particular.nro_puestos}"
)
print(
    f"Marca: {carga.marca}, Modelo: {carga.modelo}, Ruedas: {carga.nro_ruedas}, Velocidad: {carga.velocidad} Km/h, Cilindraje: {carga.cilindraje} cc, Carga: {carga.carga} Kg"
)
print(
    f"Marca: {bicicleta.marca}, Modelo: {bicicleta.modelo}, Ruedas: {bicicleta.nro_ruedas}, Tipo: {bicicleta.tipo}"
)
print(
    f"Marca: {motocicleta.marca}, Modelo: {motocicleta.modelo}, Ruedas: {motocicleta.nro_ruedas}, Tipo: {motocicleta.tipo}, Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}"
)


##################################
##           PARTE 3            ##
##################################

print("\nESTAMOS VIENDO LA PARTE 3")

import csv


def guardar_datos_csv(vehiculos, nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "w", newline="") as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                archivo_csv.writerow([vehiculo.__class__, vehiculo.__dict__])
    except Exception as e:
        print(f"Error al guardar en CSV: {e}")


def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    vehiculos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return vehiculos


# Guardar los datos de prueba en un archivo CSV
vehiculos = [particular, carga, bicicleta, motocicleta]
guardar_datos_csv(vehiculos)

# Leer los datos desde el archivo CSV y mostrarlos
vehiculos_recuperados = leer_datos_csv()
for vehiculo in vehiculos_recuperados:
    print(vehiculo)
