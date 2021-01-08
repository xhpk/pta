# #方法一
# #输入a,b,c按空格分开
# a,b,c=input("请输入三个数:").split()
# a,b,c=int(a),int(b),int(c)
# d=b*b-4*a*c
# print(d)

#方法二
x=input().split()
print(int(x[1])**2-4*int(x[0])*int(x[2]))
