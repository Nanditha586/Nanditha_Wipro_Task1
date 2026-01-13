#ordered collection of elements similar to lists but tuples are immutable
numbers=(10,20,30)
print(numbers)
fruits='apple','banana','cherry'
print(fruits)
print(fruits[1:3])
# numbers.replace(20,40) throws an error has tuple is immutable
# number.append(50) Error
print(numbers.count(30)) #it gives number times the value of 30 is present
print(numbers.index(30)) # it shows index of 30 i.e position
a=5
b=10
a,b=b,a
print(a,b)



