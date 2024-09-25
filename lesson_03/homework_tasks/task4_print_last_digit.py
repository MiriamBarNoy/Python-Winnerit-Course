"""task 4:
This code will print the last digit of any provided number """

#number to calculate
number_input1 = int((input("please enter the number to check")))


#Assertion
last_digit= abs(number_input1)%10

#Print the result
print (f"The last digit of the number provided - {number_input1} is {last_digit}" )