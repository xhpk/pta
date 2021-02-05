m=int(input())
for i in range(m):
    #定义变量表示是否为上三角
    flag=True
    n=int(input())
    #输入矩阵
    for j in range(n):
        a=list(map(int,input().split()))
        #对矩阵每一行进行检查
        for x in range(j):
            if a[x]!=0:
                flag=False
                break
    if flag:
        print("YES")
    else:
        print("NO")