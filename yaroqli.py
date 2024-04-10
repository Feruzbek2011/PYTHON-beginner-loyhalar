import re
inStr=input()
pattern ="\A([1|8|9])([0-9]{7})\Z"
match=re.match(pattern,inStr)
if match:
    print("Yaroqli")
else:
    print("Yaroqsiz")
