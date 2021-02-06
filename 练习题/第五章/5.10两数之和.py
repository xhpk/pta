lst=list(map(int,input().split(",")))
n=int(input())
#定义一个字典表示 n-lst
dir={}
for i in lst:
    dir[i]=n-i
#遍历字典判断是否存在两个数都在输入的list中
for key,value in dir.items():
    if key in lst and value in lst:
        print(lst.index(key),lst.index(value))
        break
else:
    print("no answer")
