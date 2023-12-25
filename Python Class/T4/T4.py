import random
NumberOfStudents= int(input('Enter the number of students: '))
i = 0
MinNumber = 21
MaxNumber = -1

my_list = []

while i<NumberOfStudents:
    x = random.randint(0, 20)
    my_list.append(x)
    if x<MinNumber:
        MinNumber = x
    if x>MaxNumber:
        MaxNumber = x
    i = i+1
for z in range(NumberOfStudents):
    if my_list[z]==MaxNumber:
        print(f"the index number {z} is the max")
    if my_list[z]==MinNumber:
        print(f"the index number {z} is the min")    
    
print(f'My list is: {my_list}')
print(f'Minimum number is: {MinNumber}')
print(f'Maximum number is: {MaxNumber}')