class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura = 'frio'):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon( )
        self._lavar( )
        self._centrifugar( )

    
    def _llenar_tanque_agua(self,temperatura):
        print(f'llenando el tanque con agua a {temperatura}')

    def _anadir_jabon(self):
        print("añadiendo jabón")

    def _lavar(self):
        print("lavando")

    def _centrifugar(self):
        print("centrifugando")

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar( )