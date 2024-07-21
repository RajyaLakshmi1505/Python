# Print reverse of a number using string operation
num=""
n=int(input())
while(n>0):
    r=n%10
    num=num+str(r)
    n=n//10
print(int(num)) 
#or
num1=0  
x=int(input())
while(x>0):
    m=x%10
    num1=num1*10+m
    x=x//10
print(num1)    
