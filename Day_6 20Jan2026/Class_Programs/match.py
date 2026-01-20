import re
text="python is powerful language"
result=re.match("java",text)
if result:
    print("match found")
else:
    print("no match found")
searchresult=re.search("python",text)
print(searchresult.group())