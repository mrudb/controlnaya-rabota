age = int(input("Enter your age: "))
working_exp = int(input("Enter your working experience: "))
is_cert = input("Do you have certificate: ") == "y".lower()

if is_cert == False and working_exp >= 24 and age > 21:
    print("Invite")
elif is_cert == True and working_exp >= 12 and age > 21:
    print("Invite")
else:
    print("Do not invite")