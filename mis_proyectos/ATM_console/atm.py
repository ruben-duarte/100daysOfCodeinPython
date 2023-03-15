from card_holder import cardHolder

def print_menu():
    #print options
    print("""
        Por favor escoger de las siguientes opciones:
        1. Deposito
        2. Retirar
        3. Mostrar balance
        4. Salir
    """)

def  deposit(cardHolder):
    try:
        deposit = float(input("Cuanto va a depositar :  "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Gracias por usar ATM.  Su nuevo balance: ",str(cardHolder.get_balance( )))
    except:
        print("Ingreso Invalido")


def withdraw(cardHolder):
    try:
        withdraw = float(input("Cuanto va a retirar :  "))
        #check if user has money
        if cardHolder.get_balance() < withdraw:
            print("Saldo insuficiente")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("tiene suficiente saldo para la operacion. Gracias")

    except:
        print("Ingreso Invalido")


def check_balance(cardHolder):
    print("Su saldo actual es:  ", cardHolder.get_balance())


if __name__ == "__main__":
    current_user = cardHolder("","", "", "","")

    #repo of card holders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("3456400","4532","Sara","Mendez", "500,000"))
