import random
import day3Conditional
# will include 1 and 10
random_integer = random.randint(1, 10)
# will avoid 1 and 10 exclude
print(random.randrange(1, 10))

print(random_integer)


print(day3Conditional.age)

test_sseeed = random.seed(10)

print(test_sseeed)

listNames = ["Inna", "Ruslan", "Vlad", "Julia"]
charecterFromString = "Udacha"
result = random.choice("key")
print(random.choice(listNames))
print(random.choice(charecterFromString))
print(result)
# will return random float number from 0-1 
random_float = random.random()
print(random_float)
