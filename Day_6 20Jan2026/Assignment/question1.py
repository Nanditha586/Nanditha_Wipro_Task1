import re
#1. Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)
empid=input("enter emp id ")
if re.match(r"(EMP)(\d{3})",empid):
    print("Valid employee id")
else:
    print("Invalid employee id")
#2.Uses re.search() to find the first occurrence of a valid email address in a given text
text=input("enter text")
pattern=r"([\w\.]+)@([\w]+)\.(\w+)"
email_search = re.search(pattern, text)
if email_search:
    print("Email Found")
    print("Full Email:", email_search.group(0))
else:
    print("No email found")

#3. Demonstrates the use of meta-characters (., *, +, ?) and special sequences (\d, \w, \s) in the patterns
sample_text = "Code EMP456   Age 25"
pattern = r"(EMP\d+)\s+.*?(\d{2})"
result = re.search(pattern, sample_text)
if result:
    print("Meta-characters & Special Sequences Demo")
    print("Employee Code:", result.group(1))
    print("Age:", result.group(2))
#4. Prints matched groups using capturing parentheses
text = "EMP123 employee email is john_doe@gmail.com"
pattern = r"(EMP)(\d{3}).*?([\w\.]+)@([\w]+)\.(\w+)"
match = re.search(pattern, text)
if match:
    print("Full Match :", match.group(0))
    print("Group 1 (EMP prefix):", match.group(1))
    print("Group 2 (Employee Number):", match.group(2))
    print("Group 3 (Username):", match.group(3))
    print("Group 4 (Domain):", match.group(4))
    print("Group 5 (Extension):", match.group(5))
else:
    print("No match found")