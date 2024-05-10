# Income and Employee classes inherit from the Taxpayer class
class Taxpayer:
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def calculate_total_deductions(self):
        # Abstraction
        return 0

class Income(Taxpayer):  # Inheritance
    def __init__(self, monthly_salary):
        # Attributes encapsulated within the class
        self.monthly_salary = monthly_salary

    def calculate_annual_income(self):
        return self.monthly_salary * 12  # Inheritance 

class Employee(Taxpayer):  # Inheritance
    def __init__(self, name, monthly_income, Children_allowances_per_child, number_of_children, organization_type='Corporate', is_contract_employee=False):
        super().__init__(name, monthly_income * 12)  #Superclass constructor called and attributes encapsulated
        self.Children_allowances_per_child = Children_allowances_per_child
        self.number_of_children = number_of_children
        self.organization_type = organization_type
        self.is_contract_employee = is_contract_employee

    def calculate_total_deductions(self):
        total_deductions = 0
        
        # Polymorphism
        GIS_deductions = 1000 # assuming 1000 to deduct as GIS from monthly income
        total_deductions += GIS_deductions
        
        if  self.is_contract_employee=='n':
            NPPF_deductions = 2000 # assuming 2000 NPPF_deductions as fixed for regular employee
            total_deductions += NPPF_deductions
            
        # maximun children allowance is 350000, so user can assume children allowance below 3500000 only
        total_deductions += self.Children_allowances_per_child * self.number_of_children
        
        return total_deductions


    def calculate_tax(self):
        total_deductions = self.calculate_total_deductions()
        taxable_income = self.income - total_deductions

        if taxable_income <= 300000:
            tax = 0.0 * taxable_income
        elif taxable_income <= 400001:
            tax = 0.1 * taxable_income
        elif taxable_income <= 650001:
            tax = 0.15 * taxable_income
        elif taxable_income <= 1000001:
            tax = 0.20 * taxable_income
        elif taxable_income <= 1500001:
            tax = 0.25 * taxable_income
        else:
            tax = 0.30 * taxable_income
        return tax
    
if __name__ == '__main__':
    # Object: Creating an object of the Employee class
    name = input('Enter employee name: ')
    monthly_income = float(input("Enter employee monthly income:"))
    Children_allowances_per_child = float(input('Enter children allowances per child:'))
    number_of_children = int(input('Enter number of children:'))
    organization_type = input('Enter organization type (Corporate/Private/Government):')
    is_contract_employee = input('Is the employee a contract employee? (y/n):')
    employee = Employee(name, monthly_income, Children_allowances_per_child, number_of_children, organization_type, is_contract_employee)

    # Display tax information
    tax = employee.calculate_tax()
    print(f"{employee.name} pays taxes of Nu.{tax:.2f} only.")
