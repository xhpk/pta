a=list(map(int,input().split()))
for i in range(0,3):
    print("{:4d}{:4d}{:4d}".format(a[i],a[i+3],a[i+6]))