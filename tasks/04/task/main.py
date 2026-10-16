air_pollution = float(input("Air pollution(ug/m3): "))
noise = float(input("Enter noise(dB): "))
carbon_dioxide = float(input("Carbon dioxide(ppm): "))
radiation = float(input("Radiation (uSv/h): "))
count = 0

if air_pollution > 50:
    count += 1
if noise > 70:
    count += 1
if carbon_dioxide > 400:
    count += 1
if radiation > 0.3:
    count += 1

if count == 0:
    print("Excellent")
elif count == 1:
    print("Good")
elif count == 2:
    print("Satisfactory")
elif count == 3:
    print("Poor")
elif count == 4:
    print("Very poor")
    