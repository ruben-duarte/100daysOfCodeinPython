lista = [19, 15, 15, 5, 3, 3, 5, 2]
lista = [19, 19, 5, 5, 5, 5, 5]
def  is_number19_present( ):
    for item in range(len(lista)):
        if lista[item] == 19:
             #print('true')
             return True

def number_of_5( ):
    return lista.count(5) 


def is_number5_at_least_3_times( ):
    if number_of_5() > 2:
        #print('true')
        return True
    else:
        #print('false')
        return False


# segunda manera

def check(lista):
    first_check = 19 in lista
    times_5 = lista.count(5)
    if times_5 >2 and first_check ==True:
        print('**true**')
    else:
        print('**false**')


        
is_number19_present()
is_number5_at_least_3_times()

if is_number19_present() and is_number5_at_least_3_times() ==True:
    print('true')
else:
    print('false')

check(lista)
