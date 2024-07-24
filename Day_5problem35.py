#Write a code to print all the capital letters in a given string
inp=input()
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        print(i,end="")