num=int(input())
sum=0
#定义分子分母
top=2
button=1
for i in range(0,num):
    sum+=top/button
    #分母是前一项的分子
    old_button=top
    #分子是前一项分子与分母的和
    top+=button
    button=old_button
print('{:.2f}'.format(sum))