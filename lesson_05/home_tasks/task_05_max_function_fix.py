def find_max(*args):

# List to store the added numbers
    while len(args) == 0:
        return

#check on a while in above list for the greeater number
    max_num = 0
    for i in args:
        if i > max_num:
           max_num=i
 #save the function result
    return max_num


result = find_max()
if result == None:
    print("no number provided")
else:
    print(f"the max number is {result}")
#


