#PRIME
n=int(input())
x=int(n**0.5)+1
flag=False
if(n==1):
    print("not a prime")
elif(n==2):
    print("n is a prime number")
else:        
    for i in range(2,x):
        if(n%i==0):
            flag=True
            break
    if(flag==True):
        print("n is not a prime")
    else:
        print("n is a prime number")            
    