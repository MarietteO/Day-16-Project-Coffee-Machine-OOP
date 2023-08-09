# NOTE: I only wrote the main.py. The other files were pre-written for me.
# I used ChatGPT to write the explanatory comments.

# Import necessary classes from other files.
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the CoffeeMaker and MoneyMachine classes
coffee_maker = CoffeeMaker()  # Handles coffee making and resources
money_machine = MoneyMachine()  # Handles money processing

# Initialize a flag to control the machine's state
machine_on = True

# Start the loop for processing customer orders
while machine_on:
    # Get the available menu options from the Menu class
    options = Menu().get_items()

    # Get the user's choice for their order
    choice = input(f"What would you like? {options} ")

    # Check if the user wants to turn off the machine
    if choice == "off":
        machine_on = False
    # Check if the user wants to print a report
    elif choice == "report":
        # Call the report methods of both CoffeeMaker and MoneyMachine
        coffee_report = coffee_maker.report()  # Print coffee resources status
        money_machine.report()  # Print money machine's financial status
    # Process a user's drink order
    else:
        # Access the menu
        user_choice = Menu().find_drink(choice)

        # Check if the chosen drink is available in the menu
        if user_choice:
            # Check if there are enough resources to make the chosen drink
            if coffee_maker.is_resource_sufficient(user_choice):
                # Get the cost of the chosen drink
                user_cost = user_choice.cost

                # Check if the user's payment is sufficient
                if money_machine.make_payment(user_cost):
                    # Make the coffee and deduct resources
                    coffee_maker.make_coffee(user_choice)





