class ManchesterDiferencial:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        transiciones = []
        nivel_actual = 1

        for bit in self.serial:
            if bit == '0':
                nivel_actual = -nivel_actual

            primera_mitad = nivel_actual
            segunda_mitad = -nivel_actual

            transiciones.append((primera_mitad, segunda_mitad))

            nivel_actual = segunda_mitad

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