order_amout = int(input("What's the amount?: "))

delivery_fees = 0 if order_amout >300 else 30

print(f"Delivery amount is {delivery_fees}")