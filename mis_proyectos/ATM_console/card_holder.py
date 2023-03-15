class cardHolder( ):

        def __init__(self, cardNum, pin, first_name, last_name,balance):
            self.cardNum = cardNum
            self.pin = pin
            self.first_name = first_name
            self.last_name = last_name
            self.balance = balance

        #Getters
        def get_cardNum(self):
            return self.cardNum
        def get_pin(self):
            return self.pin
        def get_first_name(self):
            return self.first_name
        def get_last_name(self):
            return self.last_name
        def get_balance(self):
            return self.balance
        
        #setters
        def set_cardNum(self, newVal):
            self.cardNum = newVal
        def set_pin(self, newVal):
            self.pin = newVal
        def set_first_name(self, newVal):
            self.first_name = newVal
        def set_last_name(self, newVal):
            self.last_name = newVal
        def set_balance(self, newVal):
            self.balance = newVal

        def print_out(self):
            print("numero de tarjeta :  ",self.cardNum)
            print("pin :  ",self.pin)
            print("nombre :  ",self.first_name)
            print("apellido :  ",self.last_name)
            print("Balance :  ",self.balance)
