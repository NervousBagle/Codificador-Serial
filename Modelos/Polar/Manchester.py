class Manchester:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        """Codifica el serial usando Manchester"""
        transiciones = []
        # Necesitamos determinar el primer nivel basado en un bit '1' previo imaginario
        # Un bit '1' va de alto a bajo, termina en bajo
        # El siguiente bit '0' iría de bajo a alto
        # El siguiente bit '1' iría de alto a bajo

        for bit in self.serial:
            if bit == '1':
                transiciones.append((1, -1))  # alto a bajo
            else:
                transiciones.append((-1, 1))  # bajo a alto
        return transiciones

    def obtener_datos_grafica(self):
        """Genera los datos para matplotlib en formato escalonado"""
        tiempo = []
        senal = []

        for i, (v1, v2) in enumerate(self.resultado):
            # Primera mitad del bit
            tiempo.append(i)
            tiempo.append(i + 0.5)
            senal.append(v1)
            senal.append(v1)

            # Segunda mitad del bit
            tiempo.append(i + 0.5)
            tiempo.append(i + 1)
            senal.append(v2)
            senal.append(v2)

        return tiempo, senal