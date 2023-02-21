# input student's mark

mark = int(input("Enter the mark: "))
if 80 <= mark <= 100:
    print("A+")
elif 70 <= mark <= 79:
    print("A")
elif 60 <= mark <= 69:
    print("A-")
else:
    print("B")
