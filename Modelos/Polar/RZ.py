class RZ:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        transiciones = []
        for bit in self.serial:
            if bit == '1':
                transiciones.append((0.5, 0))
            else:
                transiciones.append((-0.5, 0))
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