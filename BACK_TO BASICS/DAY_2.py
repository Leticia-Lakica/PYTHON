# FUNCTIONS
# A function a reusable block of code

def goodmorning(Name, Product):
    print(f"Good morning {Name}, your {Product} is ready for pickup. Hope you have a lovely day.")

goodmorning("Leticia", "blouse")
goodmorning("Malcom","Jacket")

# RETURN
# This is a statement used to end a function and send resuts back

def add(a,b):
    add = a + b
    return add

print(add(2,5))
    
def student_name(lastname, firstname):
    student_name = lastname.capitalize() + " " + firstname.capitalize()
    return student_name

print(student_name("leticia","lakica"))


# IF STATEMENTS

Is_Trash = False


if Is_Trash:
    print("Trash has been identified, preparing pickup sequence")
else:
    print("No trash detected")


name = input("Name please: ")
age = int(input("Please enter your age to access this site: "))

def age_veriication():
    if age <=0:
        print(f"Invalid age")
    elif age < 18:
        print("You are not of eligible age to access this site")
    
    else:
        print(f"Welcome to the Dark web {name}")

age_veriication()

