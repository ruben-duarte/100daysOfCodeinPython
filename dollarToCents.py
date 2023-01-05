

def  format_money(amount):
    amount = str(amount)
    zeros = ".00"
    dolar_sign = "$"
    if "." in amount:
        cents = dolar_sign + amount
        print(amount)
        print(cents)
    else:
        cents = amount + zeros
        print(cents)
    if len(amount) >=6:
        amount = amount.replace('amount[len(amount)]' , '')
        print(amount)


format_money(77)
format_money(37.00)
format_money(45.897)