class ManchesterDiferencial:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        """Codifica el serial usando Manchester Diferencial"""
        transiciones = []
        nivel_actual = 1  # Nivel donde termina el bit anterior (inicialmente arbitrario)

        for bit in self.serial:
            if bit == '0':
                # Bit 0: HAY transición al inicio (cambia respecto a donde terminó el anterior)
                nivel_actual = -nivel_actual
            # Si es '1': NO hay transición (nivel_actual no cambia)

            # El bit empieza en nivel_actual y cambia en la mitad
            primera_mitad = nivel_actual
            segunda_mitad = -nivel_actual

            transiciones.append((primera_mitad, segunda_mitad))

            # Este bit termina en segunda_mitad
            nivel_actual = segunda_mitad

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