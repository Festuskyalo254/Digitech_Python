#access control
attempts=0
trials=3
while trials<attempts:
    password=input("Enter your password: ")
    if password=="python123":
        print("Access granted.")
    else:
        print("Access denied. Try again later.") 
attempts+=1
           
