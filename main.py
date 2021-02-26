# Character Input
# import datetime
# name = input('Please enter your name: ')
# age = int(input('Please enter your age: '))
# copy = int(input('Please enter another number: '))
# now = int(datetime.datetime.now().year)
# age_turning_100 = now + (100-age)
# msg = 'Hi ' + name + ' you are going to turn 100 years old in ' + str(age_turning_100) + '.\n'
# print(msg*copy)


# Odd or Even
# num = int(input('Please enter a number: '))
# check = int(input('Please enter another number: '))
# # if num % 4==0:
# #   print(f'{num} is an even number and evenly divisible by {4}')
# # elif num % 2==0:
# #   print(f'{num} is an even number')
# # else:
# #     print(f'{num} is an odd number')
# if num % check == 0:
#   print(f'{num} is evenly divisible by {check}')
# else:
#   print(f'{num} is not evenly divisible by {check}')


# List Less Than Ten
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
print([x for x in a if x < 5])
