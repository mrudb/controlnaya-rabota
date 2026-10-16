purchase_amount = float(input("Enter purchase amount: "))
client_status = input("Client status(new/regular/vip): ")
promo = input("Enter promo: ") == "5869"
discount = 0

if purchase_amount >= 500:
    discount += 0.05
if client_status == "new":
    discount += 0.02
elif client_status == "regular":
    discount += 0.03
elif client_status == "vip":
    discount += 0.08
if promo:
    discount += 0.07

print(f"Discount: {discount * 100}%")
print(f"Payment: {purchase_amount * (1 - discount):.2f}")