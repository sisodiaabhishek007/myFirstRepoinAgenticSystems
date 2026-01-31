Balance = int(input("Enter balance amount: "))
Withdarawal = int(input("Enter amount to withdraw: "))
is_verified = input("Is user verified?: ").strip().lower()

if is_verified == "true":
    is_verified = True
elif is_verified == "false":
    is_verified = False
else:
    print("Invalid verifcation input.")
    exit()

if is_verified and Withdarawal<=Balance and Withdarawal > 0:
    print("Withdrawal successful.")
else:
    print("Transaction denied.")
