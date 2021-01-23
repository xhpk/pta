a=int(input())
sum=0
button=1
for i in range(1,a+1):
    # **表示乘n次方
    sum=sum+(i/button)*(-1)**(i+1)
    button=(button+2)
print("{:.3f}".format(sum))