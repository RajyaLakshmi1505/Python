#Remove all the brackets from the given algebraic expression
inp=input()
print(ord(')'),ord('}'),ord(']'),ord('('),ord('['),ord('{'))
for i in inp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==125 or ord(i)==123):
        pass
    else:
        print(i,end='')

