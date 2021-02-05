m,n=map(int,input().split())
a=[]
count=0
for i in range(m):
    a.append([int(n) for  n in input().split()])
#从第二行第二列遍历到倒数第二行倒数第列
for i in range(1,m-1):
    for j in range(1,n-1):
        if a[i][j]>a[i][j-1] and a[i][j]>a[i][j+1] and a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j]:
            count = 1
            print('{:d} {:d} {:d}'.format(a[i][j],i+1,j+1))
if (count== 0):
    print('None {:d} {:d}'.format(m, n))