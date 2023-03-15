#check length of 8 items in the list an the 5th item repeats at least twice

numbers_1 = [19, 19, 15, 5, 5, 5, 1, 2]
numbers_2 = [19, 15, 5, 7, 5, 5, 2]

def check(numbers, item_5):
    repeat_number = numbers.count(numbers[4])
    if repeat_number > 1 and len(numbers) == 8:
        print(True)
    else:
        print(False)

check(numbers_1, 5)
check(numbers_2,5)