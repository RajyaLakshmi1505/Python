#Print all the vowels followed by consonants
inp='helloworlsd'
str1="aeiou"
str2="bcdfghjklmnpqrstvwxyz"
ans=''
for i in inp:
    if(i in str1):
        ans=ans+i
for i in inp:        
    if(i in str2):
        ans=ans+i
print(ans)        
