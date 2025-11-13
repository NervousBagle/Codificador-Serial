class AMI:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        niveles = []
        polaridad = 0.5

        for bit in self.serial:
            if bit == '1':
                niveles.append(polaridad)
                polaridad *= -1
            else:
                niveles.append(0)

        return niveles

    def obtener_datos_grafica(self):
        tiempo = []
        senal = []

        for i, nivel in enumerate(self.resultado):
            tiempo.append(i)
            tiempo.append(i + 1)
            senal.append(nivel)
            senal.append(nivel)

        return tiempo, senal