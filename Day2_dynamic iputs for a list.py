list1=list(map(int,input().split()))
choice=int(input("Enter"))
if(choice==1):
    list1.append(23)
    print(f"appended list is {list1}")
elif(choice==2):
    list1.pop(3)
    print(f"list after popping is {list1}")
elif(choice==3):
    list1.sort()
    print(f"sorted list is {list1}")
elif(choice==4):
    print(f"length of the list is {len(list1)}")
elif(choice==5):
    print("Hello")
else:
    print("No action is done")
    


