value = input()

if value.replace('.','',1).isdigit():
    accuracy = float(value)
    print(f"Model accuracy is {accuracy}")
else:
    print("Invalid input")

