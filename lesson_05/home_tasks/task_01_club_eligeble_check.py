"""This code will check if user is eligible for club"""

#defenition of params

ticket_boolean_value = None
permission_boolean_value = None
user_age_input = input("Enter your age: ")

#enforce valid age
while user_age_input.isdigit() == False or int(user_age_input)<0 :
    user_age_input = input("Enter your age in positive numbers: ")
age = int(user_age_input)

#ticket definition
while ticket_boolean_value is None:
    has_ticket = input("Do you have ticket ? yes / no ")
    if has_ticket.lower() == "yes":
        ticket_boolean_value = True
    elif has_ticket.lower() == "no":
        ticket_boolean_value = False
    else:print("valid values are yes or no")

#permisiion - in condition needed
if 0 < age < 18:
        while permission_boolean_value is None:
            has_permission =  input("Do you have special permission ? (yes / no")
            if has_permission.lower() == "yes":
                permission_boolean_value = True
            elif has_permission.lower() == "no":
                permission_boolean_value = False
            else:print("valid values are yes or no")

match age:
    case _ if 0<age<18 and  permission_boolean_value == True:
        is_eligible = True
        print("Welcome to our club due to special permission you have")
    case _ if age > 18 and ticket_boolean_value == True:
        is_eligible = True
        print("Welcome to our club")
    case _ if (ticket_boolean_value == False) or (0<age<18 and  permission_boolean_value == True) :
        is_eligible = False
        print("You cannot join club, you are  missing minimum requirements")
    case _ :
        print("You entered invalid details we cannot join you")
