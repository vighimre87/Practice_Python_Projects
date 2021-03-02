# Odd or Even
num = int(input('Please enter a number: '))
check = int(input('Please enter another number: '))
if num % 4==0:
  print(f'{num} is an even number and evenly divisible by {4}')
elif num % 2==0:
  print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')
if num % check == 0:
  print(f'{num} is evenly divisible by {check}')
else:
  print(f'{num} is not evenly divisible by {check}')