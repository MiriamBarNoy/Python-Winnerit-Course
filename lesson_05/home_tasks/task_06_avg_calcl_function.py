def calculate_average(*args):

# check if no params
    while len(args) == 0:
        return

#check on a while in above list for the greeater number
    list_of_args = []
    total_nums = 0
    for i in args:
       list_of_args.append(i)
       total_nums += i

    avg = total_nums / len(args)

 #save the function result
    return avg

result = calculate_average(2,10,3,1) ## will be 4
if result == None:
    print("no number provided")
else:
    print(f"the avg is {result}")

result = calculate_average() ## will no numbers provided
if result == None:
    print("no number provided")
else:
    print(f"the avg is {result}")
#


