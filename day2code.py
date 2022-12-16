


arr = [1,3,7,5,9]
addition = [ ]
# 5 posibles sumas de 4 numeros
# for sum_counter in range(5):
#         for n in range(5):
#             summatory = 0   must be initialized outside the for
#             summatory = summatory + arr[n]
#         summatory - arr[sum_counter]       
#         addition.append(summatory)

# print(addition)
# for sum_counter in range(5):
#         summatory = 0
#         for n in range(5):
#             summatory += arr[n]
#         print(summatory)
#         summatory = summatory - arr[sum_counter]
#         addition.append(summatory)

# print(addition)
# ordered_sums = sorted(addition,reverse=False)
# min_sum = ordered_sums[0]
# max_sum = ordered_sums[4]

# print(min_sum, max_sum)



def miniMaxSum(arr):
    addition = []
    for sum_counter in range(5):  #5 posibles sumas de 4 elementos diferentes
        summatory = 0
        for n in range(5): # realiza la suma de 4 elementos y agrega en nueva lista
            summatory += arr[n]
        summatory -= arr[sum_counter]
        addition.append(summatory)
    ordered_sums = sorted(addition, reverse=False)
    min_sum = ordered_sums[0]
    max_sum = ordered_sums[4]
    print(min_sum, max_sum)
