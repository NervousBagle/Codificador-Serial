class Graficador:
    def __init__(self, tiempo, senal, titulo, serial_original):
        self.tiempo = tiempo
        self.senal = senal
        self.titulo = titulo
        self.serial_original = serial_original

    def obtener_datos(self):
        return {
            'tiempo': self.tiempo,
            'senal': self.senal,
            'titulo': self.titulo,
            'serial': self.serial_original
        }