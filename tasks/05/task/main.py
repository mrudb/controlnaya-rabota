summa = 0
discount = 0

while True:
    purch_amnt = input("Purchase amount(or stop): ")
    if purch_amnt == "stop":
        break
    else:
        purch_amnt = float(purch_amnt)
        summa += purch_amnt

if summa >= 200:
    discount = 0.05
elif summa >= 100:
    discount = 0.03
else:
    discount = 0

print(f"Discount rate: {discount * 100}%")
print(f"Discount: {summa * discount}")
print(f"Total: {summa * (1 - discount)}")