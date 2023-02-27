from array import *

# values = array('i',[5,9,8,7,2])  #specify type and values  

# print(values)
# print(values.buffer_info())
# print(values[1])


target = 10
arr1 = array('i', [1,2,7])
arr2 = array('i', [3,4,9])

for k in range(len(arr1)):
    for h in range(len(arr2)):
        check = arr1[k] + arr2[h]
        if check == target:
            print(f"({arr1[k]}, {arr2[h]})")

  