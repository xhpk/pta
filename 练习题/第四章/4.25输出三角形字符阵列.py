n=int(input())
cnt=65
for i in range(0,n):
    for j in range(0,n-i):
        print('{:c} '.format(cnt),end="")
        cnt=cnt+1
    print("")