n=int(input())
male=[]
female=[]
all=[]
for i in range(n):
    sex,name=input().split()
    all.append(name)
    if sex=="1":
        male.append(name)
    else:
        female.append(name)
#从高到低遍历所有学生
for i in range(int(n/2)):
    #如果是男则输出男+女最后一名
    if all[i] in male:
        print("{} {}".format(all[i],female[-1]))
        #输出之后删除最后一名
        del female[-1]
    else:
        print("{} {}".format(all[i],male[-1]))
        del male[-1]
