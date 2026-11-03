total_sales = 0
target = 500
mt = 0
bt = 0

n = int(input("Enter number of food items: "))

for i in range(1, n + 1):
    sale = int(input(f"Enter sales for item {i}: "))
    total_sales += sale

    if sale >= target:
        mt += 1
    elif sale <= target:
        bt += 1

def calculate_average():
    average = total_sales / n
    return average

def sales_report():
    print("CANTEEN SALES REPORT")
    print(f"Average sales: PHP {calculate_average()}")
    print(f"Meeting Target: {mt}")
    print(f"Below Target: {bt}")

sales_report()