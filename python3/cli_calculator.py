# A python program that handles simple calculation

operation = input('''
***********************************************
WELCOME TO THE SIMPLE CLI CALCULATOR
***********************************************
Please choose an operation you want to perform:
'+' - addition
'-' - subtraction
'x' - multiplication
'/' - division
'%' - modulus
''')

num_1 = int(input('First number: '))
num_2 = int(input('Second number: '))

# Addition
if operation == "+":
  print('{} + {} = '.format(num_1, num_2) + num_1 + num_2)