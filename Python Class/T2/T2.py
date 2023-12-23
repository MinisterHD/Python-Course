z = int(input("Enter the Number Of Students: "))
for i in range(z):
    x = int(input("Enter the score: "))

    if x < 0 or x > 20:
        print("Not Valid")
    while x < 0 or x > 20:  
        x = int(input("Enter a Valid Score: "))
    else:
        if x >= 10:
            print("Passed")
        else:
            print("Failed")
