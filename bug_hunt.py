count = 1
total = 0


# Bug: > 5 stops before adding 5, so it must be <= 5.
# Bug: the while statement was missing a colon
while count <= 5:
    total = total + count
    count = count + 1

# Bug: total is an integer, so it cannot be joined to a string with +
print("Sum of 1 to 5 is: ", total)
