class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.estado = 'en reposo'
        self.motor = Motor(cilindros = 8)

    def acelerar(self, tipo='ralenti'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self.estado = 'en movimiento'


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 15

    def inyecta_gasolina(self, cantidad):
        pass

