s=input()
m,n=input().split()
#将其转换为逆序
s=s[::-1]
for i in range(0,len(s)):
    if n==s[i]:
        print("{} {}".format(len(s)-i-1,n))
for i in range(0,len(s)):
    if m==s[i]:
        print("{} {}".format(len(s)-i-1,m))