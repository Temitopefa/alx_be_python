# Prompt the user to enter a positive integer for the size of the pattern
while True:
    size = int(input("Enter the size of the pattern: "))
    if size > 0:
        break
    else:
        print("Please enter a positive integer.")

# Use a while loop to iterate through each row of the pattern
row = 0
while row < size:
    # Use a for loop to print asterisks (*) side by side
    for _ in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    row += 1