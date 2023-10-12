print("Welcome to Dominos Pizza\n ")
size = input()
if size == "S":
    Pizza = 15
    print("Would you like to add peperon\n ")
    add_peperoni = input()

    if add_peperoni == "Y":
        Pizza += 2
    print("Would you like to add extra cheese?\n")
    add_cheese = input()
    if(add_cheese == "Y"):
       Pizza+=1     
    print( f"your total is: ${Pizza}")

elif size == "M":
    Pizza = 20
    print("Would you like to add peperon\n ")
    add_peperoni = input()


    if add_peperoni == "Y":
        Pizza += 3
    print("Would you like to add extra cheese?\n")
    add_cheese = input()
    if(add_cheese == "Y"):
       Pizza+=1    
    print( f"your total is: ${Pizza}")   

elif size == "L":
    Pizza = 25
    print("Would you like to add peperon\n ")
    add_peperoni = input()

    if add_peperoni == "Y":
        Pizza += 3
    print("Would you like to add extra cheese?\n")
    add_cheese = input()
    if(add_cheese == "Y"):
       Pizza+=1    
    print( f"your total is: ${Pizza}")    
       
