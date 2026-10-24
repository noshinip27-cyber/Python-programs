# Electricity Billing System

def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 500:
        bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + (units - 500) * 6.00

    return bill


n = int(input("Enter number of customers: "))

for i in range(1, n + 1):
    print(f"\nCustomer {i}")

    name = input("Enter customer name: ")
    units = float(input("Enter units consumed: "))

    while units < 0:
        print("Units cannot be negative.")
        units = float(input("Enter units consumed again: "))

    energy_charge = calculate_bill(units)
    fixed_charge = 50
    total_bill = energy_charge + fixed_charge

    print("\n--- Electricity Bill ---")
    print("Customer Name :", name)
    print("Units Consumed :", units)
    print("Energy Charges : Rs.", round(energy_charge, 2))
    print("Fixed Charge : Rs.", fixed_charge)
    print("Total Bill : Rs.", round(total_bill, 2))

    if total_bill >= 1000:
        print("Bill Category : High")
    else:
        print("Bill Category : Normal")
