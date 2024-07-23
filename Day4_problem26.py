#LEAP YEAR
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i%4==0 or (i%100!=0 and i%4!=0)):
        print(i,end=' ')  