n=int(input())
if(n==0):
    print('average = 0.0')
    print('count = 0')
    exit(0)
score_list=list(map(int,input().split()))
sum_score=sum(score_list)
avg_score=sum_score/n
pass_count=0
for i in score_list:
    if i>=60:
        pass_count+=1
print('average = {:.1f}'.format(avg_score))
print('count = {:d}'.format(pass_count))