n = int(input())
id_num = []
name = []
grade = []
top = 0
flag = 0
for i in range(n):
    #将学号，姓名分别存入不同数组
    temp = input().split()
    id_num.append(temp[0])
    name.append(temp[1])
    sum=0
    #方法一计算总成绩
    # grade.append(sum(list(map(int,temp[2:]))))
    #方法二
    for i in temp[2:]:
        sum+=int(i)
    grade.append(sum)
flag = grade.index(max(grade))
print(name[flag], id_num[flag], grade[flag])