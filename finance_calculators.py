import math

# Display the menu to the user
print("Menu:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Get user input and convert to lowercase for case-insensitivity
calculation_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Validate user input
if calculation_type not in ['investment', 'bond']:
    print("Invalid input. Please enter 'investment' or 'bond'.")
else:
    if calculation_type == 'investment':
        # Get user input for investment calculation
        principal_amount = float(input("Enter the amount of money you are depositing: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        years = int(input("Enter the number of years you plan on investing: "))
        interest = input("Enter 'simple' or 'compound' interest: ").lower()

        # Perform investment calculation
        if interest == 'simple':
            total_amount = principal_amount * (1 + interest_rate * years)
        elif interest == 'compound':
            total_amount = principal_amount * math.pow((1 + interest_rate), years)
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
            total_amount = None

        # Display the result
        if total_amount is not None:
            print(f"The total amount after {years} years with {interest} interest is: {total_amount}")

    elif calculation_type == 'bond':
        # Get user input for bond calculation
        present_value = float(input("Enter the present value of the house: "))
        annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
        months = int(input("Enter the number of months to repay the bond: "))

        # Calculate monthly interest rate
        monthly_interest_rate = annual_interest_rate / 12

        # Perform bond calculation
        repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

        # Display the result
        print(f"The monthly repayment amount for the bond is: {repayment}")
