# Patrón Singleton
class TrashCity:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.rutas = []
            cls._instance.observers = []
        return cls._instance

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)
        self.notificar_cambio()

    def agregar_observer(self, observer):
        self.observers.append(observer)

    def notificar_cambio(self):
        for observer in self.observers:
            observer.actualizar(self.rutas)


# Patrón Observer
class Observer:
    def __init__(self):
        pass

    def actualizar(self, rutas):
        print("Se ha actualizado la lista de rutas:")
        for ruta in rutas:
            print(f"Ruta {ruta.id_ruta}")

# Patrón Iterator
class RutaIterator:
    def __init__(self, rutas):
        self.rutas = rutas
        self.posicion = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.posicion < len(self.rutas):
            ruta = self.rutas[self.posicion]
            self.posicion += 1
            return ruta
        else:
            raise StopIteration

#Metodo para calcular total de vidrio por dia
    def cantidad_vidrio_por_dia(self, dia):
        total_vidrio = 0
        for ruta in self.rutas:
            for turno in ruta.turnos:
                if turno.dia == dia:
                    total_vidrio += turno.camion.residuos.vidrio
        return total_vidrio


class Turno:
    def __init__(self, inicio, fin, camion, dia):
        self.inicio = inicio
        self.fin = fin
        self.camion = camion
        self.dia = dia


class Ruta:
    def __init__(self, puntos, id_ruta):
        self.puntos = puntos
        self.id_ruta = id_ruta
        self.turnos = []


class Camion:
    def __init__(self, conductor, residuos, asistente1, asistente2):
        self.residuos = residuos
        self.conductor = conductor
        self.asistente1 = asistente1
        self.asistente2 = asistente2


class Residuos:
    def __init__(self, vidrio, papel, plastico, metal, organicos):
        self.vidrio = vidrio
        self.papel = papel
        self.plastico = plastico
        self.metal = metal
        self.organicos = organicos


####################################################3
#Ingresar codigo para probar:
