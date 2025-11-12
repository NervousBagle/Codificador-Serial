class Unipolar:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        """Codifica el serial usando Unipolar"""
        niveles = []
        for bit in self.serial:
            if bit == '1':
                niveles.append(0.5)
            else:
                niveles.append(0)
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