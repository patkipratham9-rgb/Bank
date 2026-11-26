name = input("Customer name: ")
balance = float(input("Initial balance: "))

deposit = float(input("Deposit amount: "))
balance = balance + deposit

withdraw = float(input("Withdraw amount: "))
balance = balance - withdraw

print("\nCustomer:", name)
print("Updated Balance: Rs.", balance)