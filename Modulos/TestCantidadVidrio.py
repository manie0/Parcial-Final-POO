#Test Funcion calculo Vidrio
from FinalPOO import *
import unittest
import io
from unittest.mock import patch

class CantidadVidrioTests(unittest.TestCase):
    def setUp(self):
        self.residuos = Residuos(2.5, 1.8, 3.2, 0.9, 4.7)
        self.camion = Camion("Juan", self.residuos, "Maria", "Pedro")
        self.turno1 = Turno("08:00:00", "16:00:00", self.camion, 1)
        self.turno2 = Turno("08:00:00", "16:00:00", self.camion, 1)
        self.trash_city = TrashCity()
        self.ruta1 = Ruta([(40.7128, -74.0060), (40.7306, -73.9352), (40.7488, -73.9857)], 1)
        self.ruta2 = Ruta([(40.7128, -74.0060), (40.7306, -73.9352)], 2)
        self.ruta1.turnos.append(self.turno1)
        self.ruta2.turnos.append(self.turno2)
        self.trash_city.agregar_ruta(self.ruta1)
        self.trash_city.agregar_ruta(self.ruta2)

    def test_cantidad_vidrio_por_dia(self):
        iterator = RutaIterator(self.trash_city.rutas)
        cantidad_vidrio = iterator.cantidad_vidrio_por_dia(1)
        self.assertEqual(cantidad_vidrio, 5)

if __name__ == "__main__":
    unittest.main()

