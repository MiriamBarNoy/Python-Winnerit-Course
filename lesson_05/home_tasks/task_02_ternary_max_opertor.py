num1_input = input("please enter first number : ")
num2_input = input("please enter second number : ")

#enforce valid age
while num1_input.isdigit() == False or  num1_input.isdigit() == False :
    num1_input = input("Please enter a valid first number as an integer: ")
    num2_input = input("Please enter a valid first number as an integer: ")
num1 = int(num1_input)
num2 = int(num2_input)

result ="larger" if num2 > num1  else "min"
if num1 == num2:
    print("numbers are equal")
elif result == "larger":
    print(f"The larger number is: {num2}")
elif result == "min":
    print(f"The larger number is: {num1}")
