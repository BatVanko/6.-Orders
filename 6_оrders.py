number_of_orders = int(input())
total_price = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    coffee_price = price_per_capsule * days * capsules_count
    print(f"The price for the coffee is: ${coffee_price:.2f}")
    total_price += coffee_price
print(f"Total: ${total_price:.2f}")
