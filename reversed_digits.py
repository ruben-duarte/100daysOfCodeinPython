

def digitize(n):
    array = []
    n = str(n)
    for digit in n:
        array.append(int(digit))
        rev_array = array[ :  :  -1]
    print(rev_array)

digitize(4534346)


def digitize(n):
    return map(int, str(n)[::-1])

digitize(4534346)

def digitize(n):
    return [int(x) for x in str(n)[::-1]]


def digitize(n):
    return list(map(int, str(n)))[::-1]