from re import match
from Controladores.GraficadorControl import GraficadorControl

import Modelos as modelos

from Modelos import Unipolar

from Modelos import Polar
from Modelos.Polar import NRZL as NRZL
from Modelos.Polar import NRZI as NRZI
from Modelos.Polar import RZ as RZ
from Modelos.Polar import Manchester as M
from Modelos.Polar import ManchesterDiferencial as MD

from Modelos import Bipolar
from Modelos.Bipolar import AMI as AMI
from Modelos.Bipolar import B8ZS as B8ZS
from Modelos.Bipolar import HDB3 as HDB3

class MainControl:
    def __init__(self):
        print("MainControl inicializado")
        # Mapeo de métodos a clases
        self.codificadores = {
            "NRZ-L": NRZL,
            "NRZ-I": NRZI,
            "RZ": RZ,
            "Manchester": M,
            "Manchester Diferencial": MD,
            "AMI": AMI,
            "B8ZS": B8ZS,
            "HDB3": HDB3,
            # etc...
        }

    def recibir_datos(self, metodo, serial):
        """Recibe los datos desde la interfaz."""
        print(".---Datos recibidos---.")
        self.remitir_datos(metodo, serial)

    def remitir_datos(self, metodo, serial):
        """Decide que metodo de codificacion se debe usar y le da los datos."""
        if metodo in self.codificadores:
            # Crear instancia del codificador
            ClaseCodificador = self.codificadores[metodo]
            codificador = ClaseCodificador(serial)

            # Obtener datos y graficar
            tiempo, senal = codificador.obtener_datos_grafica()
            GraficadorControl(tiempo, senal, metodo, serial)
        else:
            print(f"Método {metodo} aún no implementado")