
# Online Loan Eligibility Checker

# Ask the user to enter their details
income = float(input("Enter your monthly income: "))
repayments = float(input("Enter your existing monthly loan repayments: "))
credit_score = int(input("Enter your credit score (0-850): "))

# Validate the user's information
if income <= 0:
    print("Invalid input: Monthly income must be greater than zero.")

elif repayments < 0:
    print("Invalid input: Loan repayments cannot be negative.")

elif credit_score < 0 or credit_score > 850:
    print("Invalid input: Credit score must be between 0 and 850.")

else:
    # Calculate repayment-to-income ratio
    ratio = (repayments / income) * 100

    print(f"Repayment-to-income ratio: {ratio:.2f}%")

    # Check credit score
    if credit_score < 500:
        print("Loan application rejected.")

    # Check affordability
    elif repayments > 0.40 * income:
        print("Loan application rejected due to high existing repayments.")

    else:
        print("Eligible for further loan assessment.")
