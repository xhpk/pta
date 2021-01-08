s=int(input())
if s<0:
    print("Invalid Value!")
elif s<=50:
    print("cost = {:.2f}".format(0.53*s))
else:
    print("cost = {:.2f}".format(0.53*50+(s-50)*(0.53+0.05)))