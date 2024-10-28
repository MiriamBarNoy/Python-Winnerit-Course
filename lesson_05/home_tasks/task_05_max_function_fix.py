def find_max(*args):

# check if no params
    while len(args) == 0:
        return

#check on a while in above list for the greeater number
    max_num = 0
    for i in args:
        if i > max_num:
           max_num=i
 #save the function result
    return max_num


result = find_max() ## no number provided
if result == None:
    print("no number provided")
else:
    print(f"the max number is {result}")

result = find_max(2,6,5,9,8,7)  ## 9
if result == None:
        print("no number provided")
else:
        print(f"the max number is {result}")
#


