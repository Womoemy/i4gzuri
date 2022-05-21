user_no = input("Enter a number: ")

# Validation
try:
  user_no = float(user_no)
  print("Hurray, you entered a number!")

  if user_no >= 0:
    print("True")
  else:
    print("False")
  
except:
  print("False")