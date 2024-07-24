#Print upper triangular matrix
for i in range(5):
    for j in range(5):
        if(i>j):
            print("*",end='')
        else:
            print(' ')
    print()            