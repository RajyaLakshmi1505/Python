my_list=list(map(int,input().split()))
sum=0
count=0
for i in range(len(my_list)):
    if(i%2==0):
        sum+=my_list[i]
        count+=1
print(sum/count)        