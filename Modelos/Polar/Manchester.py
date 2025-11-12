class Manchester:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        """Codifica el serial usando Manchester"""
        # Manchester tiene transición en medio del bit
        # Retorna lista de tuplas (nivel1, nivel2) para cada bit
        transiciones = []
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