z = int(input("Enter the Number Of Students: "))
for i in range(z):
    x = int(input("Enter the score: "))
    
    while x < 0 or x > 20:  
        print("Not Valid")
        x = int(input("Enter a Valid Score: "))
   
    if x >= 10:
        print("Passed")
    else:
        print("Failed")
