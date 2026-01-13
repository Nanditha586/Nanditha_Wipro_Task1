from functools import reduce
#1. Uses range() to generate numbers from 1 to 20
for i in range(1,21):
    print(i)


#2. Uses filter() with a lambda to select only even numbers
even_numbers=list(filter(lambda i: i%2==0,range(1,21)))
print(even_numbers)


#3. Uses map() with a lambda to square the filtered numbers
square_of_even_numbers=list(map(lambda j:j**2,even_numbers))
print(square_of_even_numbers)

#4. Uses reduce() to calculate the sum of squared even numbers
sum_of_squared_even_numbers=reduce(lambda val,res:val+res,square_of_even_numbers)
print(sum_of_squared_even_numbers)

#5. Uses enumerate() to print the index and value of the final result list
for index,value in enumerate(square_of_even_numbers):
    print(index,value)
