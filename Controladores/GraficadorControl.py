from Modelos.Graficador import Graficador
from Vistas.GraficadorVista import GraficadorVista


class GraficadorControl:
    def __init__(self, tiempo, senal, titulo, serial_original):
        self.modelo = Graficador(tiempo, senal, titulo, serial_original)
        self.mostrar_grafica()

    def mostrar_grafica(self):
        """Crea y muestra la ventana con la gráfica"""
        datos = self.modelo.obtener_datos()
        ventana = GraficadorVista(datos)