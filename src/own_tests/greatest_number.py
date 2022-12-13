num1 = input("Num1: ")
num2 = input("Num2: ")
num3 = input("Num3: ")

if num1 > num2:
    if num1 > num3:
        print("Num1 is the greatest")
    else:
        print("Num3 is the greatest")
elif num2 > num3:
    print("Num2 is the greatest")
else:
    print("Num3 is the greatest")