amnt_of_packages = int(input("Amount of packages: "))

for i in range(amnt_of_packages):
    package_weight = float(input(f"{i + 1} Package weight: "))
    if package_weight > 10:
        continue
    else:
        print(f"Package {i + 1}: {package_weight * 30}")
