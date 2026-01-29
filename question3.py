# question 3

def powerFunction(x, y):
    return x ** y


pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
results = []

# Loop through each pair
for x, y in pairs:
    # Skip if exponent is negative
    if y < 0:
        continue

    value = powerFunction(x, y)
    results.append(value)

print(results)
