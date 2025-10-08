#optional to be handled later in class
try:
    result = 10 / 0  
except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        
#example 2 using except
try:
    number = int("123")
except ValueError:
        print("Error: Invalid input.")
else:
        print(f"Successfully converted to integer: {number}")

#finally
try:
  print(number)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
