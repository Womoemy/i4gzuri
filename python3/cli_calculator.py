# A simple calculator in Python
print("SIMPLE CLI CALCULATOR")

is_started = True

while is_started:

  operation = input("What operation would you want to perform?\nPick any of these ['+', '-', 'x', '/', '%'] : ")

  try: # Try to get user input
    num_1 = int(input('First number: '))
    num_2 = int(input('Second number: '))
  except: # if invalid return an error
    print("Failed, enter a valid number...")
    continue

  # Calculator main logic 
  if operation == "+":
    print('{} + {} = '.format(num_1, num_2) + str(num_1 + num_2))
  elif operation == "-":
    print('{} - {} = '.format(num_1, num_2) + str(num_1 - num_2))
  elif operation == "x":
    print('{} x {} = '.format(num_1, num_2) + str(num_1 * num_2))
  elif operation == "/":
    print('{} / {} = '.format(num_1, num_2) + str(num_1 / num_2))
  elif operation == "%":
    print('{} % {} = '.format(num_1, num_2) + str(num_1 % num_2))
  else:
    print("Invalid operation entered, try again...")

  # For multiple calculations
  choice = input("Would you like to run another calculation? [y,n]: ")
  if choice.upper() == "Y":
    pass
  if choice.upper() == "N":
    break # checking to see if this is the same thing as setting is_started = False

print("Thank for using the Calculator. See you later!")