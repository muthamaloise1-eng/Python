balance=12000
while balance > 0:
    withdraw = int(input("Enter amount to withdraw"))
    if withdraw > balance:
        print("insufficient balance")
    else:
        balance = balance - withdraw
        print("You have withdraw", "New balance:", balance)