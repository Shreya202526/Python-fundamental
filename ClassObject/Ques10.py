'''Assignment 10: Personal Expense Calculator

 A person wants to calculate monthly expenses and savings.

Create a class ExpenseTracker with the following attributes:

Person name

Monthly salary

Rent

Food expenses

Travel expenses

Other expenses

Create the following methods:

calculate_total_expenses() – Calculate all expenses.

calculate_savings() – Calculate salary minus total expenses.

display_expense_report() – Display salary, expenses, and savings.

Formula:

Total Expenses = Rent + Food + Travel + Other Expenses
Savings = Monthly Salary - Total Expenses

Sample data:

Monthly Salary: 60000
Rent: 12000
Food: 8000
Travel: 5000
Other Expenses: 3000

Expected result:

Total Expenses: 28000
Savings: 32000'''

class ExpenseTracker:
    def set(self,p_name,salary,rent,f_expense,t_expense,o_expense):
        self.p_name=p_name
        self.salary=salary
        self.rent=rent
        self.f_expense=f_expense
        self.t_expense=t_expense
        self.o_expense=o_expense
    def calculate_total_expenses(self):
        self.total_expense=self.rent+self.f_expense+self.t_expense+self.o_expense

    def calculate_savings(self):
        self.saving=self.salary-self.total_expense

    def display_expense_report(self):
            print("Monthly Salary:",self.salary)
            print("Rent:",self.rent)
    def display_expense_report(self):
     print("Person Name:", self.p_name)
     print("Monthly Salary:", self.salary)
     print("Rent:", self.rent)
     print("Food Expense:", self.f_expense)
     print("Travel Expense:", self.t_expense)
     print("Other Expense:", self.o_expense)
     print("Total Expenses:", self.total_expense)
     print("Savings:", self.saving)
obj = ExpenseTracker()

obj.set("Shreya", 50000, 15000, 8000, 3000, 2000)

obj.calculate_total_expenses()
obj.calculate_savings()
obj.display_expense_report()