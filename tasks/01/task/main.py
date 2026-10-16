monday = float(input("Monday: "))
tuesday = float(input("Tuesday: "))
wednesday = float(input("Wednesday: "))
thursday = float(input("Thursday: "))
friday = float(input("Friday: "))
saturday = float(input("Saturday: "))
sunday = float(input("Sunday: "))
average = (monday + tuesday + wednesday + thursday + friday + saturday + sunday) / 7

print(f"Average: {average:.2f}")
print("Days above average: ")

if monday > average:
    print("Monday")
if tuesday > average:
    print("Tuesday")
if wednesday > average:
    print("Wednesday")
if thursday > average:
    print("Thursday")
if friday > average:
    print("Friday")
if saturday > average:
    print("Saturday")
if sunday > average:
    print("Sunday")
if monday < average and tuesday < average and wednesday < average and thursday < average and friday < average and saturday < average and sunday < average:
    print("No days above average")