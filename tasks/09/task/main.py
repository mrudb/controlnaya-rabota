str1 = input("Enter text: ")

for i in range(len(str1)):
    for char in str1:
        print(f"{i}: {char}")


count = 0

while count <= len(str1):
    print(f"{count}: {str1[count]}")
    count += 1
