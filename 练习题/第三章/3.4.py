s=input()
S=input()
index=-1
for i in range(0,len(S)):
    if s==S[i]:
        if i>index:
            index=i
if index!=-1:
    print("index = {}".format(index))
else:
    print("Not Found")

#方法二使用find()查询和rfind反向查询
s,S=input(),input()
print("index = {}".format(S.rfind(s))) if S.rfind(s)!=-1 else print("Not Found")

