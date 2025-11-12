class RZ:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        """Codifica el serial usando RZ (Return to Zero)"""
        # Retorna lista de tuplas (nivel_primera_mitad, nivel_segunda_mitad)
        transiciones = []
        for bit in self.serial:
            if bit == '1':
                transiciones.append((1, 0))  # alto luego cero
            else:
                transiciones.append((0, 0))  # cero todo el tiempo
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