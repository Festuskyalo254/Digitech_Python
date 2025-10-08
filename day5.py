#loops
#we've while and for loops
#for loop

# for number in range(1,10):
#     if number%2==0:
#          print(number* "*")
   
#while loop for access control
trial=3
attempt=0
while attempt<trial:
    value=input("Enter the Password: ")
    if value=='kyalo123#':
        print("Login successful")
        break
    else:
        print("Your password is wrong try again")
        attempt+=1
else:
    print("You failed your login attempts are over")       
    