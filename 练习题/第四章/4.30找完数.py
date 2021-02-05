m,n=map(int,input().split())
flag=0
for i in range(m,n):
    l = [1]
    for x in range(2,i):
        if i%x==0:
            l.append(x)
    if sum(l)==i:
        print('{:d} = '.format(i), end="")
        l.sort()
        print(" + ".join('%s' % id for id in l))
        flag=1
if (flag == 0):
    print("None")