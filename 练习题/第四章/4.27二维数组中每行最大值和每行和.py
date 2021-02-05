a=list(map(int,input().split()))
#三个一组进行输出
for i in range(0,7,3):
    for j in a[i:i+3]:
        print('{:4d}'.format(j),end='')
    print("{:4d}{:4d}".format(max(a[i:i+3]),sum(a[i:i+3])))
