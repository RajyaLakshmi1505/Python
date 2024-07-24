#input:hello-----wor------ld
#Output:--------hello world
inp="hello----wor--ld"
inp1=''
count=0
for i in inp:
    if(i=='-'):
        count+=1
    else:
        inp1+=i
print('-'*count+inp1)        