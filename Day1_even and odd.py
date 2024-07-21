number=int(input("Enter a number"))
if (number%2==0 and number>0):
    print("Number is even and positive")
elif(number%2==0 and number<0):
    print("even and negative")
elif(number%2!=0 and number>0):
    print("odd and positive")
else:
    print("odd and negative")
