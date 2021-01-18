#去除输入中字符中的空格
s=input().replace(" ","")
a=[]
for i in s:
    if i not  in a and i.lower() not in a and i.upper() not in a:
        #判断是否为英文字母
        if i.isalpha():
            a.append(i)

if len(a)>=10:
    for i in range(0,10):
        print(a[i],end="")
else:
    print("not found")