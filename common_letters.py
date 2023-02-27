string_1 = 'naina'
sting_2  = 'adidas'

def common_letters(str1, str2 ):
    words_1 = set(str1)
    words_2 = set(str2)
    print(words_1.intersection(words_2))

common_letters('naina', 'adidas')

