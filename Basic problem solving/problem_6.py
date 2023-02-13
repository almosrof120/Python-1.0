'''
Write a program to calculate the electricity bill (accept number of unit from user) according to
the following criteria:
Unit                      Price
First 100 units         no charge
Next 100 units          Rs 5 per unit
After 200 units         Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)
'''

Bill = 0
Unit = int (input("Enter the units of electricity: "))
if Unit <= 100:
    print("No Charge.")
if 100 < Unit <= 200:
    Bill = (Unit - 100) *5
    print("The Bill amount is Rs", Bill)
if Unit > 200:
    Bill = 500 + (Unit - 200) *10
    print("The bill amount is Rs", Bill)

