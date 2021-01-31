str=input()
s="1234567890abcdefABCDEF"
a=""
for i in str:
    if i in s:
        a+=i

if len(a)==0:
    print(0)
#这里判断是否第一个十六进制字符之前存在字符 “-”
elif str.find(a[0])>str.find("-"):
    print(-int(a,16))
else:
    print(int(a,16))