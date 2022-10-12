


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
for sum_counter in range(5):
        summatory = 0
        for n in range(5):
            summatory += arr[n]
        print(summatory)
        summatory = summatory - arr[sum_counter]
        addition.append(summatory)

print(addition)

temporary = [ ]
for sum_case in range(4):
   for i in range(4):
    if addition[i] > addition[i+1]:
        addition[i] = temporary
        addition[i] =addition[i+1]
        addition[i+1] = temporary

print(addition)
