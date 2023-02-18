'''
Write a program to check whether the last digit of a number( entered by user) is
divisible by 3 or not.
'''
num = int(input("Enter the number: "))
Last_digit = num % 10
if Last_digit % 3 ==0:
    print("Divided by 3")
else:
    print("Not divided by 3.")

