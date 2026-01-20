import re
#ignorecase
text=input("enter the text")
pattern=input("enter the pattern")
match=re.search(pattern,text,re.IGNORECASE)
print("Ignore Case: ",match.group())
#multiline
text="""This
is 
the python programming"""
pattern=input("enter the pattern")
match=re.findall(pattern,text,re.MULTILINE)
print("Multiline matches: ",match)
#dotall
text = "Python\nProgramming\nWorld"

match = re.search("Python.*Programming.*World", text, re.DOTALL)
print("DOTALL Match:", match.group())

