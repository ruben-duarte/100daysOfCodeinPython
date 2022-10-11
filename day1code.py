import math
def plusMinus(arr):
    total_elements = len(arr)
    negative_elements = 0
    positive_elements = 0
    zero_elements = 0
    for n in range(total_elements):
        if arr[n] < 0 :
            negative_elements += 1
        else:
            if arr[n] == 0:
                zero_elements += 1       
    positive_elements = total_elements - (zero_elements + negative_elements )     
    ratio_positive = (positive_elements / total_elements)
    ratio_negative = (negative_elements/ total_elements)
    ratio_zeros= (zero_elements / total_elements)
    print("total elements", total_elements)    
    print("positive elements ",positive_elements)
    print("negative elements ",negative_elements)
    print("zero elements ",zero_elements)
    print('%.6f' %ratio_positive)
    print('%.6f' %ratio_negative)
    print('%.6f' %ratio_zeros, "")
    print( "ratio positive", round(ratio_positive,2))
    print("ratio positive",math.trunc(ratio_positive), end="\n") #This function is used to eliminate all decimal parts of the floating-point number and return the integer without the decimal part.
    print("ratio positive",math.ceil(ratio_positive), end="\n") #This function is used to print the least integer greater than the given number.
    print("ratio positive",math.floor(ratio_positive), end="\n") #This function is used to print the greatest integer smaller than the given integer.
    print("ratio negative",'%.3f' %ratio_negative)  #limit float precision
    print("ratio negative","%.3f" %ratio_negative)
    print("ratio negative","{0:3f}".format(ratio_negative))
    print("ratio negative",round(ratio_negative,2))


plusMinus([1,1,0,-1,-1])
