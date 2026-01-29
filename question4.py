# question 4
from random import random

# rounded to 2 decimal places for readability
values = [round(random(), 2) for i in range(20)]
x = round(random(), 2)

# Sort the list
values.sort()

matchingIndices = []

# Loop through list with index
for index, value in enumerate(values):
    if value >= x:
        matchingIndices.append(index)

print("Sorted values:", values)
print("x value:", x)

if len(matchingIndices) > 0:
    print("First matching index:", matchingIndices[0])
else:
    print("No matching value found")

