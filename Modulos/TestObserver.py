from FinalPOO import *
import unittest
from io import StringIO
from unittest.mock import patch

class ObserverTestCase(unittest.TestCase):
    def setUp(self):
        self.residuos2 = Residuos(2.5, 1.8, 3.2, 0.9, 4.7)
        self.camion2 = Camion("Juan", self.residuos2, "Maria", "Pedro")
        self.turno12 = Turno("08:00:00", "16:00:00", self.camion2, 1)
        self.turno22 = Turno("08:00:00", "16:00:00", self.camion2, 1)

        self.trash_city2 = TrashCity()

        self.observer2 = Observer()
        self.trash_city2.agregar_observer(self.observer2)

        self.ruta12 = Ruta([(40.7128, -74.0060), (40.7306, -73.9352), (40.7488, -73.9857)], 1)
        self.ruta22 = Ruta([(40.7128, -74.0060), (40.7306, -73.9352)], 2)
        self.ruta12.turnos.append(self.turno12)
        self.ruta22.turnos.append(self.turno22)

        self.trash_city2.agregar_ruta(self.ruta12)
        self.trash_city2.agregar_ruta(self.ruta22)

    def test_actualizar(self):
        expected_output = "Se ha actualizado la lista de rutas:\nRuta 1\nRuta 2\n"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.observer2.actualizar(self.trash_city2.rutas)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()