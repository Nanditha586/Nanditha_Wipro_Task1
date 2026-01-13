for i in range(1,21):
    print(i)

numbers=list(range(1,21))
evennumbers=list(filter(lambda x:x%2==0, numbers))
print(evennumbers)
