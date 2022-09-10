# real code
# Program make a funni weight calculator

print("Body Weight Calculator")

while True:
    # take input from the user
    num1 = float(input("Enter your weight (kg): "))
    
    # "calculate" the weight and output
    print("Your weight (kg): ", num1)
    
    # check if user wants another calculation
    # break the while loop if answer is no
    choice = input("Do you want to do next calculation? (yes/no): ")
    if choice in ('no'):
     break
