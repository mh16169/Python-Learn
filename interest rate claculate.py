principal_ammount = input("Enter the principal ammount:")
rate = input("Enter the rate:")
time = input("Enter the time (yearly):")

principal_ammount = float(principal_ammount)
rate = float(rate)
time = float(time)


total = principal_ammount*rate*time/100

print("The total ammount is:",total)