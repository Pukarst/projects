'''
This is my first project as the python user.'''

welcome_msg=('--->>>Welcome to my first python project (calculator)<<<---')
print(welcome_msg.upper().center(100,'-'))

number_1=float(input('Enter the first number you wish to choose--->'))
number_2=float(input('Enter the second number you wish to choose--->'))

print('The addition of the first and second number is:-',number_1+number_2)
print('The subtraction of the first and second number is:-',number_1-number_2)
print('The multiplication of the first and second number is:-',number_1*number_2)
print('The division of the first and second number is:-',number_1/number_2)
print('The remainder of the first and second number is:-',number_1%number_2)
print('The square of the first number is:-',number_1**2)
print('The cube if the first number is:-',number_1**3)
print('The square of the second number is:-',number_2**2)
print('The cube if the second number is:-',number_2**3)


end_msg=('---->>>the end<<<----')
print(end_msg.upper().center(100,'-'))