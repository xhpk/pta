a,b,c=map(lambda x:int(x),input().split())
if a+b>c and a+c>b and b+c>a:
    print("yes")
else:
    print("no")
