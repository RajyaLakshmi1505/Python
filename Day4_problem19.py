#Password verifier
#Mr.X is trying to create a new password for his new instagram account,these are the required conditions for creating a new password
#Condition-1:minimum length is 8 and max len is 15
#Condition-2:Only @,/ are allowed in a password
#Condition-3:No spaces are allowed
#Condition-4:Only alpha-numerics are allowed
#You are supposed to print weak,if length is exactly 8
#medium-if len is between 8-12
#strong-if len is between 12 to 15
new_password=input()
x=len(new_password)
if(('@' and '/') in new_password and x==8 and " " not in new_password):
    print("weak")
elif(('@' and '/') in new_password and x>8 and x<12 and " " not in new_password):
    print("Medium")
elif(('@' and '/') in new_password and x>=12 and x<=15 and " " not in new_password):
    print("Strong")
else:
    print("Follow required conditions")
#OR
              