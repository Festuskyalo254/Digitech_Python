# form input validation
print("  Sign Up Form  ")
#the inputs the program is fetching from the user
username = input("Enter your username: ")
password = input("Enter your password: ")
email = input("Enter your email: ")
name = input("Enter your name: ")
special_chars='#@$*'

if not (username and password and email and name):
    print("Error: All fields must be entered.")
elif not any(char in username for char in special_chars):
    print("Username has to contain special character")
elif len(password) < 8:
    print("Error: The password must be at least 8 characters long.")
elif '@' not in email or '.' not in email:
    print("Error: Email must be in a valid format")
    print(" ")
else:
    print("Sign up successful!")
    
        
        
    
