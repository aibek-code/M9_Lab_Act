# Aibek Abasov
# Nov 19, 2024

# Problem 1
# Write an infinite loop that prints “Infinite”.
# An infinite loop never ends.
# The condition is always true.
# After you prove to yourself that this works, comment out the code that produces the infinite loop.
# To break a loop in progress you should be able to do ctrl-C or command-C (depending on your platform).

# while True:
    print("Infinite")


# Problem 2
# Create a list L that starts with the numbers 57 and 83.
# Initialize a counter variable to 0.
# Use a while loop that runs as long as the counter is less than or equal to 10.
# On each iteration, append the current counter value to the list and increment the counter by 1.
# Stop the loop when the counter becomes greater than 10.
# After the loop, print:
# a) The total number of elements in the list.
# b) The third element in the list.

L = [57, 83]
i = 0
while i <= 10:
    L.append(i)
    i += 1

print(f"the list has {len(L)} elements")
print(f"the third element of the list is {L[2]}")

# Problem 3
# Initialize an empty list and sum variable.
# Use a while loop to ask the user for a number, append it to the list, and update the sum.
# Continue until the sum is greater than 100.

numbers = []
sum = 0

while sum <= 100:
    number = int(input("enter a number: "))
    numbers.append(number)
    sum += number

print("total sum is now gteater than 100")
print("numbers entered:", numbers)
print("final sum:", sum)
