a=input()
s=[]
for i in a:
    if i not in s:
        s.append(i)
s.sort()
for i in s:
    print(i,end="")

#方法二
#set可以去除重复
s=set(input())
y=list(s)
y.sort()
print("".join(y))