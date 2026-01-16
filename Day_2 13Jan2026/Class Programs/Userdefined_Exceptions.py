class MyError(Exception):
    pass


class Invalidage(Exception):
    pass

try:
    age=int(input("enter age"))
    if age<18:
        raise Invalidage("Age must be greater than 18 to vote")
    else:
        print("Eligible for voting")
except Invalidage as e:
    print("Error",e)
except ValueError as e:
    print("Invalid entry")
