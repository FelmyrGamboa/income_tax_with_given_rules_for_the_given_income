# Exercise 12: Calculate income tax for the given income by adhering to the rules below

# Expected Output:

# For example, suppose the taxable income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.

#Create a variable to store the value of the given taxable income
income = 45000

#Create three conditions that will evaluate the taxable income to get the income tax payable base on the given conditions
if income <= 10000:
    print("You are excempted in paying tax")

elif income <= 20000:
    payable_tax = 10000 * 0.1

else: 
    payable_tax = (10000 * 0.1) + (income - 2000) * 0.2

#Display the outcome of the computing the payable income tax