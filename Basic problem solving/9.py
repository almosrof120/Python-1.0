'''
Q1. Write a program to accept percentage from the user and display the grade according to the
following criteria:
Marks                  Grade
> 90                    A
> 80 and <= 90          B
>= 60 and <= 80         C
below 60                D
'''

Mark = int(input("Enter the mark: "))
if Mark > 90:
    print("A")
if Mark > 80 and Mark <= 90:
    print("B")
if Mark >= 60 and Mark <= 80:
    print("C")
if Mark < 60:
    print("D")
