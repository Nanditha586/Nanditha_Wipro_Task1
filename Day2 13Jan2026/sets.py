myset={1,2,2,1,3,4,5,6}
print(myset)
for i in myset:
    print(i)
myset.add(14)
print(myset)
set2={34,65,1,334}
print(myset.union(set2))
print(myset.intersection(set2))
set3=set(myset.difference(set2))
print(set3)

print(myset|set2)
print(myset & set2)
