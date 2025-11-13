class Manchester:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        transiciones = []

        for bit in self.serial:
            if bit == '1':
                transiciones.append((1, -1))  # alto a bajo
            else:
                transiciones.append((-1, 1))  # bajo a alto
        return transiciones

    def obtener_datos_grafica(self):
        tiempo = []
        senal = []

        for i, (v1, v2) in enumerate(self.resultado):
            tiempo.append(i)
            tiempo.append(i + 0.5)
            senal.append(v1)
            senal.append(v1)

            tiempo.append(i + 0.5)
            tiempo.append(i + 1)
            senal.append(v2)
            senal.append(v2)

        return tiempo, senal