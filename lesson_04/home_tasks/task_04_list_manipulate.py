"""task 2:
This code will print manipulation of a string """

#The initial list of numbers
numbers= list(range(1,17))
sum_initial_list=sum(numbers)
print(f"initial list was {numbers}")

#ommit members as required
numbers.pop(-1)
numbers.pop(0)
numbers.pop(12)
numbers.pop(7)

sum_poped = sum_initial_list-sum(numbers)

print(f"manipulated list {numbers}\n the sum of ommited numbers is {sum_poped}")