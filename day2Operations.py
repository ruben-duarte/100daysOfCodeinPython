print("#"*7)
print("Welcome to the tip calculator!")
print("#"*7)
total_bill = float(input("What was the total bill? $"))
number_people = int(input("whats the number of people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
bill_and_Tip = total_bill + total_bill*percentage/100
tip_per_person = bill_and_Tip / number_people
print("Each person should pay: $", round(tip_per_person,2))

#Data Types

#String
"Hello"
print("Hello"[2:4])
print("345" + "345")

#Integer
456
print(456 + 567)
123_456_456

#float
3.1415

#Boolean
True
False

type(456)
type("name")

number = "456"
int(number)
type(number)
45
print( )
number = input("write a number ")
first_number = int(number[0])
second_number =int(number[1])
sum = first_number + second_number
print(first_number,"+",second_number,"=", sum)
