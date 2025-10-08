
print(" Simple Access Control Check ")
print("                   ")
print("1. Admin")
print("2. Editor")
print("3. Viewer")
print("0. Exit ")
print("           ")

user_role = input("Enter your user role (0-3): ")
username =input("Enter username:  ")
if not user_role:
    print("User must have a role")
elif user_role=='1':
    print("Welcome to Admin Dash")
elif user_role=='2':
    print("Welcome to Editor's Dash")
elif user_role=='3':
    print(f"Welcome  {username}")
    
# option2
#using static defined usernames and password
print(  " Access Control  "  )
print()
username=input("Enter your Username:  ")
password=input("Enter your Password:  ")

#logic
if username=='kyalo_123' and password=='hello@123#':
    print("Welcome To Admin Dash")
else:
    print('Welcome To Customer Dash')
    

