#Replace the elements in an array with average of max and min elements
my_list=list(map(int,input().split()))
maxi=my_list[0]
mini=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
    if(my_list[i]<mini):
        mini=my_list[i]    
x=float((maxi+mini)/2)
for i in range(len(my_list)):
    my_list[i]=x
print(*my_list)    