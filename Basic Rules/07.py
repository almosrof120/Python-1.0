print("Enter salary:")
salary = input()
print("Enter year of service:")
year = input()

if int(year)>5:
    bonus = .05*int(salary)
    print("Bonus salary:",+bonus)
else:
    print("No bonus")
