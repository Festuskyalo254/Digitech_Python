# #functions
# #defining a function
def get_pass(name ,age):
    if age<=17:
        return f"{name},you are not allowed to drink"
    else:
        return f"{name},you are allowed to drink"
#generate the name and age
user_name=input("Enter you name: ")
user_age=int(input("Enter your age: "))

final=get_pass(user_name,user_age)
print(final)

#second alternative
def get_access():
    try:
        name=input("Enter your name: ")
        age =int(input("Enter your age: "))
    
        if age<=17:
                   print(f"{name}You are not allowed to drink")
        else:
             print(f"{name},You are allowed to drink")
    except ValueError:
                  print("Enter numbers not letters") 
    finally:
        print("Error handling in python")           
        
 #invoking the function
get_access()
          