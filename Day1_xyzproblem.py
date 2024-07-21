b_height=int(input("Enter height of x"))
b_weight=int(input("Enter weight of x"))
t_height=int(input("Enter height of y"))
t_weight=int(input("Enter weight of y"))
x=False
y=False
medals_of_z=int((50*14)//100) 
if(b_height==140 and b_weight%2==0):
    x=True
if((t_height>118 and t_height<148) and t_weight%medals_of_z==0):
    y=True
if(x and y):
    print("All the three players are travelling in same plane from india")
