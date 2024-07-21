y=700
a=int(input("enter a"))
b=int(input("enter b"))
o=int(input("enter o"))
v1=10*a
v2=24*b
v3=8*o
sum=a+b+o
sk=int(input("enter amount asked by shop keeper"))
if ((sk-y)>0 and sum<y):
    print("shopkeeper is a bad person")
else:
    print("shopkeeper is a good person")
