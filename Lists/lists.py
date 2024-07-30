names = ["John", "Bob", "Mosh", "Sam", "Mary"]
numbers = [1, 2, 3, 4, 5, 6]
numbers.insert(0, -1)
numbers.remove(3)
# numbers.clear()
print(1 in numbers)
print(numbers)
print(len(numbers))

# names[0] = "Jon"
first_three = names[0:3]
print(first_three)

for item in numbers:
    print("items==", item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

# for loop is better to use.

# range function in python
range_numbers = range(5, 10, 2)
print(range_numbers)
for item in range(5, 10, 2):
    print(item)
