import time
import os


class Budget:
    def __init__(self, rent, utilities, groceries, gas, amenities):
        self.rent = rent
        self.utilities = utilities
        self.groceries = groceries
        self.gas = gas
        self.amenities = amenities

    def get_budget_information(self):
        return {
            "rent": self.rent,
            "utilities": self.utilities,
            "groceries": self.groceries,
            "gas": self.gas,
            "amenities": self.amenities
        }


class Person:

    def __init__(self, name, surname, two_weekly_income, retention):
        self.name = name + " " + surname
        self.retention = float(retention)
        self.two_weekly_gross_income = float(two_weekly_income)
        self.two_weekly_net_income = 0
        self.two_weekly_expenses = 0
        self.two_weekly_savings = 0

    def get_person_information(self):
        return {
            "name": self.name,
            "retention": self.retention,
            "two_weekly_gross_income": self.two_weekly_gross_income
        }

    #
    def get_personal_calculation(self, total_per_person):
        self.two_weekly_net_income = (self.two_weekly_gross_income -
                                      (self.two_weekly_gross_income * (self.retention / 100)))
        self.two_weekly_expenses = total_per_person / 2
        self.two_weekly_savings = self.two_weekly_net_income - self.two_weekly_expenses
        return {
            "name": self.name,
            "retention": self.retention,
            "two_weekly_expenses": self.two_weekly_expenses,
            "two_weekly_gross_income": self.two_weekly_gross_income,
            "two_weekly_net_income": self.two_weekly_net_income,
            "two_weekly_savings": self.two_weekly_savings,
            "monthly_expenses": self.two_weekly_expenses * 2,
            "monthly_gross_income": self.two_weekly_gross_income * 2,
            "monthly_net_income": self.two_weekly_net_income * 2,
            "monthly_savings": self.two_weekly_savings * 2
        }


def set_participants():
    number_of_participants = input("How many people are at home? ")
    if not number_of_participants.isnumeric():
        print("Hey! Introduce a valid integer number...")
        set_participants()
    else:
        participants = []
        number_of_participants = int(number_of_participants)
        for participant in range(0, number_of_participants):
            person = Person(input(f"""Name of holder nº{participant + 1}: """),
                            input(f"""Surname of holder nº{participant + 1}: """),
                            input(f"""Two weekly gross income of holder nº{participant + 1}: """),
                            input(f"""Retention percentage of holder nº{participant + 1}: """)
                            )
            participants.append(person)
        return participants


def set_budget():
    rent_price = input("Which is the monthly rent?")
    while not rent_price.isnumeric():
        print("Hey! Introduce a valid number...")
        rent_price = input("Which is your monthly rent?")
    else:
        rent_price = float(rent_price)

    utilities_price = input("How much for the utilities expenses?")
    while not utilities_price.isnumeric():
        print("Hey! Introduce a valid number...")
        utilities_price = input("How much for the utilities expenses?")
    else:
        utilities_price = float(utilities_price)

    groceries_price = input("How much are your monthly groceries expenses?")
    while not groceries_price.isnumeric():
        print("Hey! Introduce a valid number...")
        groceries_price = input("How much are your monthly groceries expenses?")
    else:
        groceries_price = float(groceries_price)

    gas_expenses = input("How much are your monthly gas expenses?")
    while not gas_expenses.isnumeric():
        print("Hey! Introduce a valid number...")
        gas_expenses = input("How much are your monthly gas expenses?")
    else:
        gas_expenses = float(gas_expenses)

    amenities_expenses = input("How much are your monthly amenities expenses? (Eat Out/Gym/Cinema)")
    while not amenities_expenses.isnumeric():
        print("Hey! Introduce a valid number...")
        amenities_expenses = input("How much are your monthly amenities expenses? (Eat Out/Gym/Cinema)")
    else:
        amenities_expenses = float(amenities_expenses)

    return Budget(rent_price, utilities_price, groceries_price, gas_expenses, amenities_expenses)


def calculate(members, budget):
    total = 0
    for expense in budget.get_budget_information().values():
        total += expense
    total_per_person = total / len(members)
    calculation_per_person = []
    for member in members:
        calculation_per_person.append(member.get_personal_calculation(total_per_person))
    return calculation_per_person


def main():
    data = calculate(set_participants(), set_budget())
    document = open(f"""budget_{round(time.time() * 1000)}.txt""", "a")
    for person in data:
        for key, value in person.items():
            document.write(f"""{key}: {value}\n""")
        document.write("\n")
    document.close()
    path_name = os.getcwd()
    print(f"""Document generated in {path_name}""")


main()
