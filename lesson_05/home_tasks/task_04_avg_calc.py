#define needed
total = 0
number = 0

#Requere the numbers in loop and add them to the total variable
for i in range(0,5):
    number = int(input(f"Enter number {i + 1} : "))
    total += number

# Calculate the average
avg = total / 5

print(f"The average is:{avg}")
