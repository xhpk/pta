a = {"+":"x+y","-":"x-y","*":"x*y","/":"x/y"}
x = float(input())
op = input()
y = float(input())
try:
    print("{:.2f}".format(eval(a[op])))
except:
    print("divided by zero")