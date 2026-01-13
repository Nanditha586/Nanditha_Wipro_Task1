from debugpy.server.cli import switches

print("For loop")
for i in range(1,11):
    print(i)
print("While loop")
j=15
while j<=20:
    print(j)
    j=j+1
print("Switch")
day=int(input("Enter your day:"))
match day:
    case 1:print("Day is Monday")
    case 2:print("Day is Tuesday")
    case 3:print("Day is Wednesday")
    case 4:print("Day is Thursday")
    case 5:print("Day is Friday")
    case 6:print("Day is Saturday")
    case 7:print("Day is Sunday")

print("Break and continue")
for i in range(1,11):
    if i==5:
        continue
    if i==9:
        break
    print(i)