class NRZI:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        niveles = []
        nivel_actual = 1

        for bit in self.serial:
            if bit == '1':
                nivel_actual *= -1
            niveles.append(nivel_actual)

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