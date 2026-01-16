numbers=[23,54,12,33,1]
names=['raju','ravi','raghu']
mixed=['raghav',1,0.8,True]
print(numbers.count(23))
print(numbers.index(1))
print(numbers)
print(names)
print(mixed)
for i in numbers:
    print(i)
if 'ravi' in names:
    print("ravi is found in names")
matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])
names.reverse()
print(names)
names.append("rajesh")
print(names)
names.extend(["pavan","leela"])
print(names)
names.remove("rajesh")
print(names)
names.insert(2,"ramu")
print(names)
