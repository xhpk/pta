def acronym(p):
    s=""
    #用title将首字母大写
    p=p.title()
    a=p.split()
    for i in range(0,len(a)):
        s=s+a[i][0]
    return s

phrase=input()
print(acronym(phrase))