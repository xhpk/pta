n = int(input())
a, b = 1, 0
if n<1:
    print("Invalid.")
else:
    for i in range(n):
        if (i+1)%5!=0:
            print("{:11d}".format(a),end="")
        else:
            print("{:11d}".format(a))
        #计算前两项和
        b,a=a,a+b
