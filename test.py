import random

list = ["1", "2", "3", "4"]
hey = ""
bello = ""
for char in range(1, 5):
    hey = random.choice(list)
    list.remove(hey)
    bello = hey + bello
print(list)
print(bello)