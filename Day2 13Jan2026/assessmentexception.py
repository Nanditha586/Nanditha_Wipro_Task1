import math

def division_of_twonums(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        return "Divide by zero error occurred"
    except ValueError as e:
        return f"An err occurred: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def square_root(c):
    try:
        if c<0:
            raise ValueError("Negative integer")
        return math.sqrt(c)
    except ValueError:
        return "Square root of a negative number is undefined."
    except Exception as e:
        return f"An error occurred: {e}"
if __name__ == "__main__":
    try:
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        num=int(input("Enter num value: "))
        division_value=division_of_twonums(num1,num2)
        sqroot=square_root(num1)
        print(division_value)
        print(sqroot)
    except ValueError:
        print("Invalid input format")

