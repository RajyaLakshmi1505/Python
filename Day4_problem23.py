#LCM
#Relation between LCD, GCD, TWO NUMBERS A AND B IS (A*B)=(LCD*GCD) 
a=int(input())
b=int(input())
y=a*b
while(b!=0):
    a,b=b,a%b
print("GCD=",a)
print("LCD=",y//a)