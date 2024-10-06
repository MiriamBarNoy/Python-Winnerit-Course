"""task 2:
This code will print manipulation of a string """

#define the string
str_to_manipulate = input("please enter the sentence to change ")

# Print required indexed chars
print(f"Lowercase {(str_to_manipulate.lower())}")
print(f"Uppercase {str_to_manipulate.upper()}")
print(f"Capitalized {str_to_manipulate.capitalize()}")
print(f"Title case  {str_to_manipulate.title()}")
print(f"The words of your sentence are  {str_to_manipulate.split()}")
