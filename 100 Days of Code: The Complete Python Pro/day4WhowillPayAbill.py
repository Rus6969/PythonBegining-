import random

names = ["Inna", "Alan", "Kate", "Anastasia", "Tamara", "valrntine"]
number_of_names = len(names)

random_choice = random.randint(0, number_of_names-1)

print(names[random_choice])

l1 = ["Ruslan"]
l2 = ["Samatov"]
l3 = l1+l2
print(l3)

# nested list
fruits = ["apple", "pear"]
vegie = ["cucumber", "spinach"]
combined = [fruits, vegie]
print(combined)
