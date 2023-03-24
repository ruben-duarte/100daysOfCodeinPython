str_1 = 'watermelon'
str_2 = 'melon'

def common_letters(str_1, str_2):
    set_1 = set(str_1)
    set_2 = set(str_2)
    unique_letters = set_1 & set_2
    return list(unique_letters)

a = common_letters(str_1, str_2)
print(a)