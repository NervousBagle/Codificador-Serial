from tkinter import messagebox


class HDB3:
    def __init__(self, serial):
        self.serial = serial
        self.serial_validado = self._validar_serial(4)
        if not self.serial_validado:
            messagebox.showwarning("Advertencia",
                                   "HDB3 requiere al menos una secuencia de 4 ceros en el serial para poder codificarlo")
            self.resultado = []
            return
        self.resultado = self.codificar()

    def _validar_serial(self, validacion):
        contador_ceros = 0
        for bit in self.serial:
            if bit == '0':
                contador_ceros += 1
            if contador_ceros >= validacion:
                return True
        return False

    def codificar(self):
        signal = []
        polaridad = -0.5
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

                if contador_ceros == 4:
                    base = len(signal) - 4

                    if contador_unos_desde_sustitucion % 2 == 0:
                        signal[base + 0] = polaridad
                        signal[base + 3] = polaridad
                    else:
                        signal[base + 3] = -polaridad

                    contador_ceros = 0
                    contador_unos_desde_sustitucion = 0

        return signal

    def obtener_datos_grafica(self):
        tiempo = []
        senal = []

        for i, nivel in enumerate(self.resultado):
            tiempo.append(i)
            tiempo.append(i + 1)
            senal.append(nivel)
            senal.append(nivel)

        return tiempo, senal