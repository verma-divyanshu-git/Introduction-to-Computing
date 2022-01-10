#question 2
gross_income=float(input("Gross income: "))
tax_rate=20/100
standard_deduction=10000
deduction_per_dependent=3000
number_of_dependent=int(input("Number of dependents: "))
taxable_income= gross_income - standard_deduction - (deduction_per_dependent*number_of_dependent)
#calculating tax
tax=taxable_income*tax_rate
print("your income tax is: " ,tax)
