s=input()
m,n=input().split()
# s=s[::-1]
for i in range(0,len(s)):
    if n==s[i]:
        print("{} {}".format(len(s)-i,n))
for i in range(0,len(s)):
    if m==s[i]:
        print("{} {}".format(i,m))