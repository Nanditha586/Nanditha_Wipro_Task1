#count unique characters
def Count(s):
    result=[]
    star_count=s.count("*")
    question_count=s.count("?")
    star_char=chr(ord('a')+ star_count-1)
    question_char=chr(ord('a')+ question_count-1)
    result.append(star_char)
    result.append(question_char)
    return result
S=input("enter the string")
result=Count(S)
print(" ".join(str(x) for x in result))