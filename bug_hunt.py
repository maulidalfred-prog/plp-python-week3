count = 1
total = 0

# BUG: The while statement was missing a colon.
# BUG: The condition stopped before adding 5, so it must include 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an integer, so it must be converted to a string.
print("Sum of 1 to 5 is: " + str(total))