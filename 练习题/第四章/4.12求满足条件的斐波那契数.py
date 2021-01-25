num=int(input())
first=1
second=1
f=0
while f<num:
    f=first+second
    first=second
    second=f
print(f)