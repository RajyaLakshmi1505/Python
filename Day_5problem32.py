#Print the unique characters in a string
i=input()
int=i.lower()
str=''
for i in int:
    if(i not in str):
        str+=i
print(str)        