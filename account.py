# name = input("Customer name: ")
# balance = float(input("Initial balance: "))

# deposit = float(input("Deposit amount: "))
# balance = balance + deposit

# withdraw = float(input("Withdraw amount: "))
# balance = balance - withdraw

# print("\nCustomer:", name)
# print("Updated Balance: Rs.", balance)

MIN_BALANCE = 2000

name = input("Customer name: ")
balance = float(input("Initial balance: "))

deposit = float(input("Deposit amount: "))
balance = balance + deposit

withdraw = float(input("Withdraw amount: "))
if balance - withdraw < MIN_BALANCE:
    print("Withdrawal denied: Minimum balance of Rs. 2000 required.")
else:
    balance = balance - withdraw

print("\nCustomer:", name)
print("Updated Balance: Rs.", balance)