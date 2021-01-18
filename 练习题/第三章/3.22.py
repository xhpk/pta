str=input()
s=""
for i in str:
    if i.isupper() and i not in s:
        s+=i
if len(s)>0:
    for i in  s:
        print(i,end="")
else:
    print("Not Found")