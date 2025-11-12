class Codificador():
    def __init__(self, serial):
        self.serial = serial
        self.resultado = self.__procesar_serial(serial)

    def __procesar_serial(self, serial):
        return self.resultado