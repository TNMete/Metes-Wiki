start_price = 4.30
km = int(input("bitte Kilometer eingeben :"))
if km < 5:
    costs = 2.5
else: 
    costs = 2.1
costs = 2.10
total_expenses = start_price + costs * km
print("zu zahlen :", total_expenses, "€")