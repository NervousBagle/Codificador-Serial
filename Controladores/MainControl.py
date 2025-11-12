from re import match

import Modelos
class MainControl:

    def __init__(self):
        print("MainControl inicializado")

    def recibir_datos(self, metodo, serial):
        """Recibe los datos desde la interfaz."""
        print(".---Datos recibidos---.")
        self.remitir_datos(metodo, serial)

    def remitir_datos(self, metodo, serial):
        """Decide que metodo de codificacion se debe usar y le da los datos."""
        match(metodo):
            case "Unipolar":
                pass
            case "Manchester":
                pass
            case "Manchester Diferencial":
                pass
            case "NRZ-I":
                pass
            case "NRZ-L":
                pass
            case "RZ":
                pass
            case "AMI":
                pass
            case "B8ZS":
                pass
            case "HDB3":
                pass
