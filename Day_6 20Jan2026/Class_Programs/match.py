import re
text="python is powerful language"
result=re.match("java",text)
if result:
    print("match found")
else:
    print("no match found")
searchresult=re.search("language",text)
print(searchresult.group())
print(searchresult.start())
print(searchresult.end())

email="abc01@gmail.com"
if re.match(r"[a-zA-Z0-9]+@+gmail.com",email):
    print("valid email")
else:
    print("invalid email")

result2=re.fullmatch(r"\d{10}",'123456780')
print(result2)

print(re.findall(r"\d+","price is 50 and 100 only")) #only digits
print(re.findall(r"\w+","price is 50 and 100 only")) #alphanumeric
print(re.findall(r"\D+","price is 50 and 100 only")) #only alphabets
print(re.findall(r"\W+","price is 50 and 100 only")) #nonalphanumeric

for n in re.finditer(r"\d+","A1, B33, C444"):
    print(n.group(),n.start(),n.end())