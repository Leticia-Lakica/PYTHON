# LOOPS
# 1. FOR LOOPS
# For loops execute a block of code a fixed number of times

name = input("Enter your name: ")

for i in reversed(range(1,10)):
    print(i)

print(f"Happy new year {name}!")

password = "qwerty1234"

for i in password:
    print(i)

# WHILE LOOPS
# A while loop will execute a block of code while a condition is true
print("Welcome to Vmovies")


age =int(input("Please enter your age to start: ")) 
while age<0 or age>75:
    print(f"{age} are not eligible to access this site")
    age = int(input("Please enter your age to start: ")) 

movie = input("What movie would you like to watch today: ")

while movie == "":
    print("Please enter a movie title")
    movie = input("What movie would you like to watch today: ")

print(f"Please standyby as we coonect to a server to play {movie}")



print("Server 1")
print("Server 2")
print("Server 3")
print("Server 4")
print("Server 1")
print("q to quit")

option = input("Please select one of the servers: ")

if not option == "q":
    print(f"{option} is loading please wait")
else:
    print("See you next time")
