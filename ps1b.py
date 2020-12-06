import math
annual_salary = input("enter your annual salary:")
portion_saved = input("enter the percent of your salary to save, as a decimal:")
total_cost = input("enter the cost of your dream home:")
semi_annual_raise = input("enter the semi-annual rase, as a decimal:")

current_savings = 0
rate_of_return = .04
number_of_months = 0

current_savings = float(current_savings)
annual_salary = float(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)
portion_down_payment = total_cost*.25
semi_annual_raise = float(semi_annual_raise)

while current_savings < portion_down_payment:
    current_savings = current_savings+rate_of_return*current_savings/12
    current_savings = current_savings+portion_saved*annual_salary/12
    number_of_months = number_of_months+1
    if(number_of_months%6==0):
        annual_salary = annual_salary+semi_annual_raise*annual_salary
print ("number of months:",number_of_months)