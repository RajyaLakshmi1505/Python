#Print the element at a particular index : cycling printing
#k=20
#10 20 30 40 50
#  1  2  3  4
k=int(input())
my_list=list(map(int,input().split()))
x=int(len(my_list))
if(k<x):
    print(my_list[x])
else:
    print(my_list[(k-1)%x])
