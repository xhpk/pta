x=input()
for i in x:
    if i.isupper():
        i=i.lower()
    elif i.islower():
        i=i.upper()
    elif i=='#':
        break
    print(i,end="")

#方法二
print(input()[0:-1].swapcase())