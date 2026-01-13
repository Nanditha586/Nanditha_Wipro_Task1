data = [1, 2, 3, 4, 5, 6, 2, 4]
#1. Create a list comprehension to store squares of all numbers
square=[x**2 for x in data]
print(square)
#2. Create a set comprehension to store only unique even numbers
unique_even_numbers={x for x in data if x%2==0}
print(unique_even_numbers)

#3. Create a dictionary comprehension where the key is the number and the value is its cube
cubes={num:num**3 for num in data}
print(cubes)