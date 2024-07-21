#Find the duplicates in an array and print duplicate list and without duplicates list
my_list=list(map(int,input().split()))
new_list1=[]
duplicates=[]
for i in my_list:
    if(i not in new_list1):
        new_list1.append(i)
    else:
        duplicates.append(i)
print(*new_list1)
print(*duplicates)