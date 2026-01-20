def make_it_equal(A,B):
    if '%' not in A:
        if A==B:
            return ""
        else:
            return -1
    prefix,suffix=A.split('%')
    if not B.startswith(prefix) or not B.endswith(suffix):
        return -1
    start_index=len(prefix)
    end_index=len(B)-len(suffix)
    replacement=B[start_index:end_index]
    return replacement
t1=input("enter the string t1")
t2=input("enter the string t2")
result=make_it_equal(t1,t2)
print(result)

