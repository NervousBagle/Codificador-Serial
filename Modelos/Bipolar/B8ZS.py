from tkinter import messagebox

class B8ZS:
    def __init__(self, serial):
        self.serial = serial
        self.serial_validado = self._validar_serial(8)
        if not self.serial_validado:
            messagebox.showwarning("Advertencia",
                                   "B8ZS requiere al menos una secuencia de 8 ceros en el serial para poder codificarlo")
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

        for bit in self.serial:
            if bit == '1':
                polaridad *= -1
                signal.append(polaridad)
                contador_ceros = 0
            else:
                contador_ceros += 1
                signal.append(0)

                if contador_ceros == 8:
                    ultima_polaridad = polaridad
                    base = len(signal) - 8
                    signal[base + 0] = 0
                    signal[base + 1] = 0
                    signal[base + 2] = 0
                    signal[base + 3] = ultima_polaridad
                    signal[base + 4] = -ultima_polaridad
                    signal[base + 5] = 0
                    signal[base + 6] = -ultima_polaridad
                    signal[base + 7] = ultima_polaridad
                    contador_ceros = 0

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