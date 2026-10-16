days = int(input("Enter days: "))
liters = 100

for i in range(days):
    if liters <= 20:
        break
    consume_per_day = float(input("Enter consume per day: "))
    liters -= consume_per_day

if liters <= 20:
    print(f"Days: {i}")
else:
    print(f"Days: {days}")
print(f"Water left: {liters} l")
