#5:5 *patterns
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()#next line  
# ****
#* ***
#** **
#*** *
#****
for i in range(5):
    for j in range(5):
        if(i==j):
            print(' ',end='')
        else:
            print('*',end='')    
    print()  
