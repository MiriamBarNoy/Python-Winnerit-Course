from itertools import count


def find_max(*args):

# List to store the added numbers
    added_nums = []
    count_i = int(input("Enter the number of values you want to check for max: "))
    while count_i == 0:
        return
 # Use a for loop with range to collect each number and add it to the list
    for i in range(count_i):
        num_input = int(input(f"Enter number {i + 1}: "))
        added_nums.append(num_input)
        max_num = added_nums[0]

#check on a while in above list for the greeater number
    for i in added_nums:
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


