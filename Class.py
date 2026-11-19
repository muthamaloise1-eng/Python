a = 10
print(a)

mylist = [24, 31, 77]
print(len(mylist))

print("Numbers from 0:9", list(range(9)))

#fee balance
#sem_fee =30000
#fee_paid = int(input("Please enter amount paid:"))
#balance = sem_fee-fee_paid
#if balance <= 0:
 #   print("Balance is:" ,balance, "sit for exam")
#else:
 #   print("Balance is:", balance, "You cannot sit for exam")


#Another code

age = int(input("Enter your age"))
if age < 0:
    print("Invalid age")
elif age >= 0 and age < 18:
    print("0 - 17 years")
elif age >= 18 and age <= 25:
    print("18 - 25")
elif age <= 25 and age <= 30:
    print("26 - 30")
else:
    print(">30")