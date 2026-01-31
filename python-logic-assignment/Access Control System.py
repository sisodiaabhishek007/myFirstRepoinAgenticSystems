age = int(input("Enter your age: "))
has_ID = input("Have ID ?: ").strip().lower()

if has_ID == "true":
    has_ID = True
elif has_ID == "false":
    has_ID = False
else:
    print("Invalid input for ID. Please enter either True or False.")
    exit()

if age >=18 and has_ID:
    print("Entry allowed")
else:
    print("entry not allowed")
