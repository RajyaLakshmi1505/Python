#Print XYZ if input is ABC and EFG if ABC
inp='ABC'
char=''
n=0
for  i in inp:
    n=ord(i)
    char+=chr(n+4*6-1)
print(char,end=" ") 
#INPUT:ABC,OUTPUT;EFG
char2=''
for  i in inp:
    n=ord(i)
    char2+=chr(n+4)
print(char2,end=" ")  
#INPUT:XYZ,OUTPIT:ABC
inp1='XYZ'
char1=''
n=0
for  i in inp1:
    n=ord(i)
    char1+=chr(n-(4*6-1))
print(char1)  

    