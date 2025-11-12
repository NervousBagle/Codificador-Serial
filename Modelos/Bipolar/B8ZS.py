class B8ZS:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        """Codifica el serial usando B8ZS (Bipolar with 8-Zero Substitution)"""
        signal = []
        polaridad = 1
        contador_ceros = 0

        for bit in self.serial:
            if bit == '1':
                polaridad *= -1
                signal.append(polaridad)
                contador_ceros = 0
            else:
                contador_ceros += 1
                signal.append(0)

                # Si hay 8 ceros consecutivos, aplicar patrón 000VB0VB
                if contador_ceros == 8:
                    ultima_polaridad = polaridad
                    base = len(signal) - 8
                    signal[base + 0] = 0
                    signal[base + 1] = 0
                    signal[base + 2] = 0
                    signal[base + 3] = ultima_polaridad  # V
                    signal[base + 4] = -ultima_polaridad  # B
                    signal[base + 5] = 0
                    signal[base + 6] = -ultima_polaridad  # V
                    signal[base + 7] = ultima_polaridad  # B
                    contador_ceros = 0

        return signal

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