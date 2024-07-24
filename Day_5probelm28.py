#Check how many vowels and consonants are there in a string
i=input()
inp=i.lower()
check="aeiou"
alpha="bcdfghjklmnpqrstvwxyz"
vowel_count=0
cons_count=0
for i in inp:
    if(i in check):
        vowel_count+=1 
    if(i in alpha):
        cons_count+=1
print(vowel_count)   
print(cons_count)         