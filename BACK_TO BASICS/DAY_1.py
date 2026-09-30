# VARIABLES
# This is basically a container used for storing values

# WAYS TO PRINT VARIABLES IN PYTHON

# Year = 2026

# print("The projected will be completed by " + str(Year) + " as promised")
# print("The project will be completed by", Year, "as promised")
# print(f"The project will be completed by {Year} as promised")

# TYPES OF VARIABLES
# 1. Intergers
x=5
print(x)

# 2. STRINGS
Name = "Mitchelle"

print(f"Welcome to our webpage {Name}")

# BOOLEAN
is_present = False

if is_present:
    print(f"{Name} is in attaendance today")
else:
    print(f"{Name} is absent")

# Boolean are case sensitive and shoulnt be placed in quotes other wise they will be read as strings by the system

#4. FLOAT - these are numbers with decimal places
gpa = 4.8
print(f"{Name} has a {gpa}")