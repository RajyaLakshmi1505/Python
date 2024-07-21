#Find the missing number in an array
my_list=[1,2,3,5,6,7,8,9,10]
n=len(my_list)
total_sum=((n+1)*(n+2))/2
sum=0
for i in range(len(my_list)): 
    sum+=my_list[i]
print(total_sum-sum)
#OR    
#for i in range(len(my_list)):
#    if(my_list[i+1]!=my_list[i]+1):
#        print(my_list[i+1]-1)