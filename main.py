class Main:
    def __init__(self):
        self.income_dict = {}
        self.expense_dict = {}
        self.total_investments_dict = {}

    def income_revenue(self):
        income_sources = input("What is one source of income you have? ")
        income_sources_exp = int((input(f"How much {income_sources} do you get within a month? ")))
        self.income_dict[income_sources] = income_sources_exp
    
    def expense_payments(self):
        expense_sources = input("What is one source of expense you have? ")
        expense_sources_exp = int((input(f"How much does {expense_sources} cost you every month? ")))
        self.expense_dict[expense_sources] = expense_sources_exp

    def total_investments(self):
        investment_sources = input("What is one major investment you have? ")
        investment_sources_exp = int((input(f"How much did you pay for {investment_sources}? ")))
        self.total_investments_dict[investment_sources] = investment_sources_exp

    def show(self):
        user_input = input("Enter 1 to see your list of incomes, 2 to see your list of expenses, or 3 to see your list of investments ")
        if user_input == "1":
            print(self.income_dict)
        elif user_input == "2":
            print(self.expense_dict)
        elif user_input == "3":
            print(self.total_investments_dict)
        else:
            print("Please choose a valid option!")
    
    def modify_elements(self):
        user_input = input("Enter 1 to modify your list of incomes, 2 for your list of expenses, or 3 for your list of investments ")
        if user_input == '1':
            income_key = input("What source of income would you like to change? ")
            for i in self.income_dict.keys():
                if income_key == i:
                    income_value = int(input("What do you want to change that cost to? "))
                    self.income_dict[i] = income_value
        if user_input == '2':
            expense_key = input("What source of expense would you like to change? ")
            for x in self.expense_dict.keys():
                if expense_key == x:
                    expense_value = int(input("What do you want to change that cost to? "))
                    self.expense_dict[x] = expense_value
        if user_input == '3':
            investment_key = input("What source of investment would you like to change? ")
            for j in self.total_investments_dict.keys():
                if investment_key == j:
                    investment_value = int(input("What do you want to change that cost to? "))
                    self.total_investments_dict[j] = investment_value       

class Calculator(Main):
    def cash_flow_calc(self):
        annual_cash_flow = (sum(self.income_dict.values()) - sum(self.expense_dict.values())) * 12
        return annual_cash_flow

    def calculator_for_ROI(self):
        print(f"Your annual cash flow is {Calculator.cash_flow_calc(self)}.")

        total_investment_sum = sum(self.total_investments_dict.values())
        roi_num = (Calculator.cash_flow_calc(self) / total_investment_sum) * 100
        print(f"Your ROI is {round(roi_num, 2)}%.")

obj1 = Calculator()
                     
def run():
    while True:
        user_input = input("""
            Looking to calculate your rental property's return on investment? We are happy to help here at Bigger Pockets!
            Choose the following: 
            1. Add a source of income
            2. Add a source of expense
            3. Add an investment made for your property
            4. Modify
            5. Show the list of income, expenses, and investments you have
            6. Calculate your ROI
            7. Quit/Exit
            """)
        if user_input == '7':
            print("Thanks for using our services...we'll bill you next time though!")
            break
        elif user_input == '1':
            obj1.income_revenue()
        elif user_input == '2':
            obj1.expense_payments()
        elif user_input == '3':
            obj1.total_investments()
        elif user_input == '4':
            obj1.modify_elements()
        elif user_input == '5':
            obj1.show()
        elif user_input == '6':
            obj1.calculator_for_ROI()
        else:
            print("Please enter a valid number item 1-5 for the list of choices available")
run()