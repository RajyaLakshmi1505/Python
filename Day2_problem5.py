list1=list(map(int,input().split(" ")))
count_even=0
count_odd=0
for i in list1:
    if (i%2==0) :
        count_even+=1
    else:
        count_odd+=1
print(f"even={count_even}")   
print(f"odd={count_odd}")         