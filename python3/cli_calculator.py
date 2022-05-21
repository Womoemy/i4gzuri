# A python program that handles simple calculation

operation = input('''
SIMPLE CLI CALCULATOR
***********************************************
Choose an operation you want to perform:
Pick any of these ['+', '-', 'x', '/', '%']

''')

num_1 = int(input('First number: '))
num_2 = int(input('Second number: '))

if operation == "+":
  print('{} + {} = '.format(num_1, num_2) + str(num_1 + num_2))
elif operation == "-":
  print('{} - {} = '.format(num_1, num_2) + str(num_1 - num_2))
elif operation == "x":
  print('{} x {} = '.format(num_1, num_2) + str(num_1 * num_2))
elif operation == "/":
  print('{} / {} = '.format(num_1, num_2) + str(num_1 / num_2))
else:
  print('{} % {} = '.format(num_1, num_2) + str(num_1 % num_2))