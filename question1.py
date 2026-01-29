# Question 1

# variables names and values
threshold = 100
product = 1
currentNumber = 1

# Loop to multiply numbers until product exceeds threshold
while product <= threshold:
    product = product * currentNumber
    currentNumber = currentNumber + 1

# Print results
print("Final product:", product)
print("Number that exceeded threshold:", currentNumber - 1)
