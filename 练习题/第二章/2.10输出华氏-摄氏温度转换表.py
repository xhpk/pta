a,b=input().split()
a=int(a)
b=int(b)
if a>b:
    print("Invalid.")
else:
    print("fahr celsius")
    for i in range(a,b+1,2):
        c=5*(a-32)/9
        print("{}{:6.1f}".format(a,c))
        a = a + 2