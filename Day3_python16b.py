#Find the sum of even digits
sum=0
n=int(input())
while(n>0):
    r=n%10
    if(r%2==0):
        sum+=r
    n=n//10
print(sum) 