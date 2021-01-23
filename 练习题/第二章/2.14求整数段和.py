# a,b=input().split()
a,b=map(lambda x:int(x),input().split())
a=int(a)
b=int(b)
sum=0
count=0
for i in range(a,b+1):
    print("{:5d}".format(i),end="")
    count=count+1
    sum=sum+i
    if count%5==0:
        print()
if count%5!=0:
    print()
print("Sum = {}".format(sum))