# name = input("Enter your name: ")
# age = input("Enter your age: ")

# weight = input("Enter your weight in pounds: ")

# weight_in_kg = float(weight) * 0.454
# print(name + ' weighs ' + str(weight_in_kg) + ' kg')


# FORMATTED STRINGS
# first_name = "Leticia"
# last_name = "Smith"
# message = f"{first_name} [{last_name}] is a coder"
# print(message)

# ARITHEMETIC OPERATIONS
# print(10/3)

# X = (2+3)* 10-3
# print(X)

# IF STATEMENTS
# price = 1000000
# credit_is_good = True
# credit_is_bad = False

# if credit_is_good:
#     print(f"Put a down payment : {0.1* price}")
# else:
#     print(f"Put down payment:{0.2 * price}")
    

# name = input("Enter your name: ")
# if len(name)<3:
#     print("Name must be atleast 3 characters long")
# elif len(name)>50:
#     print("Name must be a maximum of 50 characters")

# else:
#     print("Name looks good")

# Weight = input('Weight: ')

# weight_in_kgs = float(Weight) * 0.454
# weight_in_lbs = float(Weight) / 0.454

# convert_weight = input('(L)bs or (K)g: ').lower()

# if convert_weight == "k":
#     print(f'You weigh {str(weight_in_lbs)} pounds')
# elif convert_weight == "l":
#     print(f' You weigh {str(weight_in_kgs)} Kilograms')
# else:
#     print("Invalid option")

# WHILE LOOPS

game_running = True
while game_running == True:
 option = input().lower()
 
 if option == "help":
    print('Start - to Start car')
    print('Stop car')
    print('Quit')
    option = input("select an option: ").lower()
    
 elif option == "Start":
   print("The car has started")
   break
 elif option == "Stop":
   print("The car has stopped")
   break
 elif option == "Quit":
   break
   
 else:
   print("I dont understand that")

