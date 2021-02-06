lst=list(map(int,input().split(",")))
a=[]
for i in range(6,11):
    if i not in lst:
        a.append(i)
print(*a)