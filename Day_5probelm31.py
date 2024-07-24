#Input:hello123world output:6
input='hello123world'
numbers='1234567890'
sum=0
x=0
for i in input:
    if(i in numbers):
        sum+=int(i)
print(sum) 