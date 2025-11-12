class HDB3:
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.codificar()

    def codificar(self):
        """Codifica el serial usando HDB3 (High-Density Bipolar 3-Zero)"""
        signal = []
        polaridad = 1
        contador_ceros = 0
        contador_unos_desde_sustitucion = 0

        for bit in self.serial:
            if bit == '1':
                polaridad *= -1
                signal.append(polaridad)
                contador_ceros = 0
                contador_unos_desde_sustitucion += 1
            else:
                contador_ceros += 1
                signal.append(0)

                # Si hay 4 ceros consecutivos, aplicar regla HDB3
                if contador_ceros == 4:
                    base = len(signal) - 4

                    if contador_unos_desde_sustitucion % 2 == 0:
                        # B00V -> marca al inicio y violación al final
                        signal[base + 0] = polaridad
                        signal[base + 3] = polaridad
                    else:
                        # 000V -> solo violación al final (polaridad opuesta)
                        signal[base + 3] = -polaridad

                    contador_ceros = 0
                    contador_unos_desde_sustitucion = 0

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