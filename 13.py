'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

'''

AI = int(input("Enter the AI result: "))
if AI >= 80:
    print("A+")
if AI >= 70:
    print("A")
if AI >= 60:
    print("A-")
if AI >= 50:
    print("B")
if AI >= 40:
    print("C")
if AI >= 33:
    print("D")
else:
    print("Fail")
    