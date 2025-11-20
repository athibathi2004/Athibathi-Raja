a = int(input("Enter a number: "))

# Find the largest odd number ≤ a → this decides how many odd numbers to print
if a % 2 == 0:
    count = a - 1
else:
    count = a

# Now generate 'count' odd numbers
result = []
num = 1

for i in range(count):
    result.append(num)
    num += 2

print(*result, sep=", ")
