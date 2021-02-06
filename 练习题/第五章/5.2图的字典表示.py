n=int(input())
num=0
sum=0
for i in range(n):
    #将每一行输入变为字典
    dic=eval(input())
    #遍历每一行内容
    for j in dic:
        temp=dic[j]
        for key in temp:
            num+=1
            sum+=temp[key]
print("{:d} {:d} {:d}".format(n,num,sum))