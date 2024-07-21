import math
n=int(input())
count=0
x=int(math.sqrt(n))
for i in range(2,x+1):
    if(n%i==0):
        count+=1    
if(count>0):
    print("Composite")
else:
    print("Prime")        
