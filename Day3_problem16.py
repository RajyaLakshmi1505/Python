# Print sum of digits in a number and sum of square of digits
sum=0
squared_sum=0
n=int(input())
while(n>0):
    r=n%10
    sum=sum+r
    squared_sum+=r*r
    n=n//10
print(sum)   
print(squared_sum)
