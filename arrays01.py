array_1 = [1, 3, 4, 5]
array_2 = [2, 4, 6, 8]

#Given two sorted arrays, the task is to merge them in a sorted manner.

merge_array = array_1 + array_2


for item in range(len(merge_array)-1):
    if  merge_array[item + 1] < merge_array[item]:
        temp = 0
        temp = merge_array[item]
        merge_array[item] = merge_array[item + 1]
        merge_array[item + 1] = temp


sorted_array = merge_array.sort()
print(merge_array)
print(sorted_array)
