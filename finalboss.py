import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
let = ""
for char in range(1, nr_letters + 1):
    let =  random.choice(letters) + " " + let
num = ""
for char in range(1 , nr_numbers + 1):
    num = random.choice(numbers)  + " " + num
sym = ""
for char in range(1 , nr_symbols + 1):
    sym = random.choice(symbols)  + " " + sym

password = let + num + sym
passlist = password.split(" ")
rangee = nr_letters + nr_symbols + nr_numbers
hey = ""
bello = ""

for char in range(1, rangee + 2):
    hey = random.choice(passlist)
    passlist.remove(hey)
    bello = hey + bello

print(bello)