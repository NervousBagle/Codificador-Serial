from Controladores.GraficadorControl import GraficadorControl

from Modelos.Unipolar import Unipolar

from Modelos.Polar.NRZL import NRZL
from Modelos.Polar.NRZI import NRZI
from Modelos.Polar.RZ import RZ
from Modelos.Polar.Manchester import Manchester
from Modelos.Polar.ManchesterDiferencial import ManchesterDiferencial

from Modelos.Bipolar.AMI import AMI
from Modelos.Bipolar.B8ZS import B8ZS
from Modelos.Bipolar.HDB3 import HDB3

class MainControl:
    def __init__(self):
        print("MainControl inicializado")
        # Mapeo de métodos a clases
        self.codificadores = {
            "Unipolar": Unipolar,
            "NRZ-L": NRZL,
            "NRZ-I": NRZI,
            "RZ": RZ,
            "Manchester": Manchester,
            "Manchester Diferencial": ManchesterDiferencial,
            "AMI": AMI,
            "B8ZS": B8ZS,
            "HDB3": HDB3,
        }

    # Obtiene los datos de la vista.
    def recibir_datos(self, metodo, serial):
        self.remitir_datos(metodo, serial)

    # Decide que metodo de codificacion se debe usar y le da los datos.
    def remitir_datos(self, metodo, serial):
        if metodo in self.codificadores:
            ClaseCodificador = self.codificadores[metodo]
            codificador = ClaseCodificador(serial)
            tiempo, senal = codificador.obtener_datos_grafica()
            GraficadorControl(tiempo, senal, metodo, serial)
        else:
            print(f"Método {metodo} aún no implementado")