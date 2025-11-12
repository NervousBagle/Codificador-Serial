class NRZL:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        """Codifica el serial usando NRZ-L"""
        niveles = []
        for bit in self.serial:
            if bit == '1':
                niveles.append(-1)  # Cambiar de 1 a -1
            else:
                niveles.append(1)   # Cambiar de -1 a 1
        return niveles

    def obtener_datos_grafica(self):
        """Genera los datos para matplotlib en formato escalonado"""
        tiempo = []
        senal = []

        for i, nivel in enumerate(self.resultado):
            tiempo.append(i)
            tiempo.append(i + 1)
            senal.append(nivel)
            senal.append(nivel)

        return tiempo, senal