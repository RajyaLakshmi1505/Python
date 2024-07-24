#Print the sum of integers  in a string using ord()
input='hello1234world'
sum=0
for i in input:    
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)