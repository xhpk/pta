s=input()
#定义一个空字符串
a=""
for i in s:
    #用isdigital函数判断是否为数字
    if i.isdigit():
        #为数字则连接起来
        a+=i
print(int(a))