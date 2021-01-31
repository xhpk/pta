n = int(input())
weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
count= 0
dic = {0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
for i in range(n):
    m=input()
    s=[]#用于后面求和
    if not m[0:17].isdigit():
        print(m)
        count+=1
    else:
        for x in range(17):
            s.append(int(m[x])*weight[x])
        if dic[sum(s)%11]!=m[17]:
            print(m)
            count+=1
if count==0:
    print("All passed")