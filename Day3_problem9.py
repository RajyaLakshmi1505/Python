#Find the elements that is present in (k+n)th index
#Test case:1
# Sample input:k is given by user ,k=3
#n=2
#inputs=3 6 8 4 61 2
#op is 2
#Test case:2
# k=3
#n=4
#inputs=80 70 54 36 72
#op is ERROR
n=int(input())
k=int(input())
my_list=list(map(int,input().split()))
x=int(len(my_list))
if(x<n+k):
    print("ERROR")
else:
    for i in range(0,x):
        break
print(my_list[k+n])        
           