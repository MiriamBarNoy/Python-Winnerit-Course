"""task 3:
This code will assert two given digits can both be divided by 7 """

#given numbers definition
number_input1,number_input2 = (input("please enter 2 numbers to check")).split()
number_input_split = int(number_input1)
number_input_split2 = int(number_input2)

#Assertion
is_divided = number_input_split % 7 == 0 and number_input_split2 % 7 == 0

#Print the result
print (f"The answer if {number_input_split} & {number_input_split2} can be both divide by 7 is {is_divided} " )