"""task 1:
This code will print specific chars in string by index """

#define the string
str_to_check = input("please enter a word to check ")

# Print required indexed chars
print(f"The first char on string is {str_to_check[0]}")
print(f"The last char on string is {str_to_check[-1]}")
print(f"The middle char on string is {str_to_check[len(str_to_check)//2]}")
print(f"The odd chars on string is {str_to_check[1::2]}")
print(f"The even chars on string is {str_to_check[0::2]}")
print(f"The string in reverse {str_to_check[::-1]}")
